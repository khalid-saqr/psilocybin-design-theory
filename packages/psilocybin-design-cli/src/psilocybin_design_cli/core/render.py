from __future__ import annotations

import shutil
from importlib.resources import files
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from psilocybin_design_cli.constants import DESIGN_FILENAME, REQUIRED_GENESIS_FILES
from psilocybin_design_cli.core.validate import assert_renderable, validate_design
from psilocybin_design_cli.io import write_text, write_yaml

PACKAGE = "psilocybin_design_cli"

TEMPLATE_MAP = {
    "README.md": "README.md.j2",
    "AGENTS.md": "AGENTS.md.j2",
    "CLAUDE.md": "CLAUDE.md.j2",
    ".github/copilot-instructions.md": "copilot-instructions.md.j2",
    "DESIGN.md": "DESIGN.md.j2",
    "IMPLEMENTATION_SEQUENCE.md": "IMPLEMENTATION_SEQUENCE.md.j2",
    "SURVIVAL_TESTS.md": "SURVIVAL_TESTS.md.j2",
    "docs/genome.md": "genome.md.j2",
    "docs/organism.md": "organism.md.j2",
    "docs/ontology.md": "ontology.md.j2",
    "docs/stack-rationale.md": "stack-rationale.md.j2",
    "docs/decision-memory.md": "decision-memory.md.j2",
}


def template_env() -> Environment:
    template_dir = files(PACKAGE) / "templates" / "genesis"
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(enabled_extensions=()),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def project_slug(design: dict) -> str:
    name = (design.get("project", {}) or {}).get("name") or "psilocybin-project"
    return str(name).strip().replace(" ", "-").lower()


def render_genesis_repo(design: dict, output_dir: Path, *, allow_warnings: bool = False) -> Path:
    report = validate_design(design)
    assert_renderable(report, allow_warnings=allow_warnings)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    env = template_env()
    context = {"design": design, "project_slug": project_slug(design)}
    for rel_path, template_name in TEMPLATE_MAP.items():
        template = env.get_template(template_name)
        text = template.render(**context).rstrip() + "\n"
        write_text(output_dir / rel_path, text)

    write_yaml(output_dir / DESIGN_FILENAME, design)
    write_text(
        output_dir / "tests" / "survival" / "README.md",
        env.get_template("SURVIVAL_TESTS.md.j2").render(**context).rstrip() + "\n",
    )
    verify_required_files(output_dir)
    return output_dir


def verify_required_files(output_dir: Path) -> None:
    missing = [rel for rel in REQUIRED_GENESIS_FILES if not (output_dir / rel).exists()]
    if missing:
        raise FileNotFoundError(f"Generated repo is missing required files: {missing}")
