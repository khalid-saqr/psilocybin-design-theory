from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import httpx
import typer
import yaml
from rich.table import Table

from psilocybin_design_cli import __version__
from psilocybin_design_cli.config import load_config, save_workspace_config, set_dotted
from psilocybin_design_cli.constants import DESIGN_FILENAME
from psilocybin_design_cli.core.pack import pack_genesis_repo
from psilocybin_design_cli.core.render import render_genesis_repo, project_slug
from psilocybin_design_cli.core.session import (
    create_workspace,
    find_workspace,
    load_design,
    outputs_dir,
    resolve_design_file,
    save_design,
    suggestions_dir,
    workspace_for_design_file,
)
from psilocybin_design_cli.core.stages import require_stage
from psilocybin_design_cli.core.validate import validate_design
from psilocybin_design_cli.errors import LLMError, WorkspaceError
from psilocybin_design_cli.io import console
from psilocybin_design_cli.llm.guardrails import validate_suggestion_contract
from psilocybin_design_cli.llm.ollama import OllamaClient
from psilocybin_design_cli.llm.openai_compatible import OpenAICompatibleClient
from psilocybin_design_cli.llm.prompts import build_prompt

app = typer.Typer(help="Psilocybin Genesis CLI: create agent-readable genesis repositories.", no_args_is_help=True, invoke_without_command=True)


def abort(message: str, code: int = 1) -> None:
    console.print(f"[red]ERROR[/red] {message}")
    raise typer.Exit(code)


def make_client(cfg: dict):
    llm_cfg = cfg.get("llm", {})
    provider = llm_cfg.get("provider", "ollama")
    if provider == "ollama":
        return OllamaClient(
            base_url=llm_cfg.get("base_url", "http://localhost:11434"),
            model=llm_cfg.get("model", "qwen3:4b"),
            temperature=float(llm_cfg.get("temperature", 0.2)),
            top_p=float(llm_cfg.get("top_p", 0.8)),
        )
    if provider == "openai-compatible":
        return OpenAICompatibleClient(
            base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
            model=llm_cfg.get("model", "local"),
            api_key=llm_cfg.get("api_key", "local"),
            temperature=float(llm_cfg.get("temperature", 0.2)),
            top_p=float(llm_cfg.get("top_p", 0.8)),
        )
    raise LLMError(f"Unknown LLM provider: {provider}")


def print_report(report, *, as_json: bool = False) -> None:
    if as_json:
        console.print(json.dumps(report.to_dict(), indent=2))
        return
    table = Table(title="Psilocybin Design Validation")
    table.add_column("Status")
    table.add_column("Gate")
    table.add_column("Message")
    for msg in report.messages:
        style = {"pass": "green", "warning": "yellow", "error": "red"}[msg.severity]
        label = {"pass": "PASS", "warning": "WARN", "error": "FAIL"}[msg.severity]
        table.add_row(f"[{style}]{label}[/{style}]", msg.name, msg.message)
    console.print(table)


@app.callback()
def main(version: bool = typer.Option(False, "--version", help="Show package version and exit.")) -> None:
    if version:
        console.print(__version__)
        raise typer.Exit(0)


@app.command()
def init(
    name: str = typer.Argument(..., help="Project name."),
    force: bool = typer.Option(False, "--force", help="Overwrite existing workspace."),
    no_llm: bool = typer.Option(False, "--no-llm", help="Disable LLM assistance in workspace config."),
) -> None:
    """Create a new design workspace."""
    try:
        workspace = create_workspace(name, force=force, llm_enabled=not no_llm)
    except WorkspaceError as exc:
        abort(str(exc))
    console.print(f"[green]Created workspace:[/green] {workspace}")
    console.print(f"Design memory: {workspace / DESIGN_FILENAME}")


@app.command()
def interview(
    stage: Optional[str] = typer.Option(None, "--stage", help="Interview only one stage."),
    file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path."),
) -> None:
    """Collect structured deterministic inputs."""
    design_path = resolve_design_file(file)
    design = load_design(design_path)
    stages = [stage] if stage else [
        "project", "gap", "language", "verbs", "relations", "invariants", "genome",
        "organism", "ontology", "survival", "death", "stack", "sequence", "agents",
    ]
    for st in stages:
        require_stage(st)
        console.print(f"\n[bold]Stage: {st}[/bold]")
        if st == "project":
            raw = input("What do you want to build? ").strip()
            if raw:
                design["project"]["raw_intention"] = raw
            outcome = input("What outcome should this software make possible? ").strip()
            if outcome:
                design["project"]["desired_outcome"] = outcome
        elif st == "gap":
            design["gap"]["failed_relation"] = input("What relation is failing? ").strip() or design["gap"].get("failed_relation", "")
            design["gap"]["missing_possibility"] = input("What becomes impossible because of this? ").strip() or design["gap"].get("missing_possibility", "")
        elif st == "language":
            phrases = input("Repeated phrases around the gap, separated by ';': ").strip()
            if phrases:
                design["language_game"]["repeated_phrases"] = [p.strip() for p in phrases.split(";") if p.strip()]
            workarounds = input("Workarounds, separated by ';': ").strip()
            if workarounds:
                design["language_game"]["workarounds"] = [p.strip() for p in workarounds.split(";") if p.strip()]
        else:
            console.print("This stage can be completed manually in YAML or through `psilocybin suggest` + `psilocybin accept`.")
    save_design(design_path, design)
    console.print(f"[green]Updated[/green] {design_path}")


@app.command()
def validate(
    file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path."),
    strict: bool = typer.Option(False, "--strict", help="Treat warnings as errors."),
    json_output: bool = typer.Option(False, "--json", help="Print report as JSON."),
) -> None:
    """Validate schema and traceability."""
    try:
        design = load_design(file)
        report = validate_design(design, strict=strict)
        print_report(report, as_json=json_output)
    except Exception as exc:
        abort(str(exc), code=2)
    if report.errors:
        raise typer.Exit(1)


@app.command()
def render(
    file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path."),
    output: Optional[Path] = typer.Option(None, "--output", help="Output genesis-repo directory."),
    allow_warnings: bool = typer.Option(False, "--allow-warnings", help="Render even if validation has warnings."),
) -> None:
    """Render the genesis-repo directory."""
    try:
        design = load_design(file)
        out = output or outputs_dir(file) / f"{project_slug(design)}-genesis"
        render_genesis_repo(design, out, allow_warnings=allow_warnings)
        console.print(f"[green]Rendered genesis-repo:[/green] {out}")
    except Exception as exc:
        abort(str(exc))


@app.command()
def pack(
    file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path."),
    output: Optional[Path] = typer.Option(None, "--output", help="Output zip path."),
    allow_warnings: bool = typer.Option(False, "--allow-warnings", help="Pack even if validation has warnings."),
) -> None:
    """Render and zip a genesis-repo."""
    try:
        design = load_design(file)
        outs = outputs_dir(file)
        repo_dir, zip_path = pack_genesis_repo(design, outs, output_zip=output, allow_warnings=allow_warnings)
        console.print(f"[green]Rendered:[/green] {repo_dir}")
        console.print(f"[green]Packed:[/green] {zip_path}")
    except Exception as exc:
        abort(str(exc))


@app.command()
def suggest(
    stage: str = typer.Argument(..., help="LLM suggestion stage."),
    file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path."),
) -> None:
    """Ask the optional local LLM for structured suggestions."""
    try:
        require_stage(stage, llm=True)
        design_path = resolve_design_file(file)
        workspace = workspace_for_design_file(design_path)
        cfg = load_config(workspace)
        if not cfg.get("llm", {}).get("enabled"):
            abort("LLM assistance is disabled. Run `psilocybin config set llm.enabled true`.")
        design = load_design(design_path)
        client = make_client(cfg)
        prompt = build_prompt(stage, design)
        data = client.complete_json(prompt)
        validate_suggestion_contract(data)
        out = suggestions_dir(design_path) / f"{stage}.suggestion.json"
        out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        console.print(f"[green]Wrote suggestion:[/green] {out}")
    except Exception as exc:
        abort(str(exc))


@app.command()
def accept(
    stage: str = typer.Argument(..., help="Suggestion stage to accept."),
    file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path."),
    all: bool = typer.Option(False, "--all", help="Accept all suggestions without interactive prompts."),
) -> None:
    """Accept, edit, or reject pending LLM suggestions."""
    try:
        require_stage(stage, llm=True)
        design_path = resolve_design_file(file)
        design = load_design(design_path)
        suggestion_path = suggestions_dir(design_path) / f"{stage}.suggestion.json"
        if not suggestion_path.exists():
            abort(f"No suggestion found: {suggestion_path}")
        data = json.loads(suggestion_path.read_text(encoding="utf-8"))
        validate_suggestion_contract(data)
        accepted = 0
        for suggestion in data.get("suggestions", []):
            console.print(f"\n[bold]{suggestion.get('id')}[/bold] -> {suggestion.get('target_path')}")
            console.print(f"Reason: {suggestion.get('reason')}")
            console.print(yaml.safe_dump(suggestion.get("value"), sort_keys=False, allow_unicode=True))
            choice = "y" if all else input("Accept? [y]es / [n]o: ").strip().lower()
            if choice not in {"y", "yes"}:
                continue
            target = suggestion["target_path"]
            value = suggestion.get("value", {})
            if isinstance(design.get(target), list):
                design[target].append(value)
            elif isinstance(design.get(target), dict) and isinstance(value, dict):
                design[target].update(value)
            else:
                design[target] = value
            accepted += 1
        save_design(design_path, design)
        console.print(f"[green]Accepted {accepted} suggestion(s).[/green]")
    except Exception as exc:
        abort(str(exc))


config_app = typer.Typer(help="Manage CLI configuration.")
app.add_typer(config_app, name="config")


@config_app.command("show")
def config_show() -> None:
    try:
        workspace = None
        try:
            workspace = find_workspace()
        except WorkspaceError:
            pass
        cfg = load_config(workspace)
        console.print(yaml.safe_dump(cfg, sort_keys=False))
    except Exception as exc:
        abort(str(exc))


@config_app.command("set")
def config_set(
    key: str,
    value: str,
    user: bool = typer.Option(False, "--user", help="Write user config instead of workspace config."),
) -> None:
    try:
        if user:
            from psilocybin_design_cli.config import save_user_config
            cfg = load_config(None)
            set_dotted(cfg, key, value)
            save_user_config(cfg)
            console.print("[green]Updated user config.[/green]")
        else:
            workspace = find_workspace()
            cfg = load_config(workspace)
            set_dotted(cfg, key, value)
            save_workspace_config(workspace, cfg)
            console.print(f"[green]Updated workspace config:[/green] {workspace / '.psilocybin' / 'config.yaml'}")
    except Exception as exc:
        abort(str(exc))


@app.command()
def doctor(file: Optional[Path] = typer.Option(None, "--file", help="Design YAML path.")) -> None:
    """Check environment, workspace, templates, schemas, and optional LLM runtime."""
    table = Table(title="Psilocybin Genesis CLI Doctor")
    table.add_column("Check")
    table.add_column("Status")
    table.add_column("Detail")
    table.add_row("version", "PASS", __version__)
    try:
        design_path = resolve_design_file(file)
        table.add_row("workspace", "PASS", str(design_path.parent))
        load_design(design_path)
        table.add_row("design_yaml", "PASS", str(design_path))
        cfg = load_config(design_path.parent)
    except Exception as exc:
        table.add_row("workspace", "WARN", str(exc))
        cfg = load_config(None)
    llm_cfg = cfg.get("llm", {})
    if not llm_cfg.get("enabled"):
        table.add_row("llm", "WARN", "LLM assistance disabled; deterministic CLI remains usable.")
    else:
        provider = llm_cfg.get("provider")
        base_url = llm_cfg.get("base_url")
        model = llm_cfg.get("model")
        try:
            if provider == "ollama":
                response = httpx.get(f"{str(base_url).rstrip('/')}/api/tags", timeout=5)
                response.raise_for_status()
                names = [m.get("name") for m in response.json().get("models", [])]
                if model in names:
                    table.add_row("ollama_model", "PASS", str(model))
                else:
                    table.add_row("ollama_model", "WARN", f"{model} not found. Available: {', '.join(names) or 'none'}")
            else:
                table.add_row("llm_provider", "WARN", f"Provider {provider} configured; endpoint not deeply checked.")
        except Exception as exc:
            table.add_row("llm_runtime", "WARN", f"Could not reach configured LLM runtime: {exc}")
    console.print(table)
