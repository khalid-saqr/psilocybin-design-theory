from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from psilocybin_design_cli.config import DEFAULT_CONFIG, save_workspace_config
from psilocybin_design_cli.constants import DESIGN_FILENAME, SCHEMA_VERSION
from psilocybin_design_cli.errors import WorkspaceError
from psilocybin_design_cli.io import read_yaml, write_yaml
from psilocybin_design_cli.model import DesignSession


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", name.strip()).strip("-._")
    if not slug:
        raise WorkspaceError("Project name must contain at least one alphanumeric character.")
    return slug.lower()


def default_design(name: str = "") -> dict[str, Any]:
    session = DesignSession()
    data = session.model_dump(mode="json")
    data["schema_version"] = SCHEMA_VERSION
    data["project"]["name"] = name
    return data


def create_workspace(name: str, *, force: bool = False, llm_enabled: bool | None = None) -> Path:
    slug = slugify(name)
    workspace = Path.cwd() / f"{slug}.design"
    if workspace.exists() and not force:
        raise WorkspaceError(f"Workspace already exists: {workspace}. Use --force to overwrite.")
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "suggestions").mkdir(exist_ok=True)
    (workspace / "outputs").mkdir(exist_ok=True)
    (workspace / ".psilocybin").mkdir(exist_ok=True)
    design = default_design(slug)
    save_design(workspace / DESIGN_FILENAME, design)
    cfg = DEFAULT_CONFIG.copy()
    cfg["llm"] = dict(DEFAULT_CONFIG["llm"])
    if llm_enabled is not None:
        cfg["llm"]["enabled"] = llm_enabled
    save_workspace_config(workspace, cfg)
    return workspace


def find_workspace(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    if cur.is_file():
        cur = cur.parent
    for candidate in [cur, *cur.parents]:
        if (candidate / DESIGN_FILENAME).exists():
            return candidate
    raise WorkspaceError("No psilocybin.design.yaml found in current directory or parents.")


def resolve_design_file(file: Path | None = None, workspace: Path | None = None) -> Path:
    if file is not None:
        return file.resolve()
    ws = workspace or find_workspace()
    return ws / DESIGN_FILENAME


def load_design(file: Path | None = None) -> dict[str, Any]:
    path = resolve_design_file(file)
    data = read_yaml(path)
    try:
        DesignSession.model_validate(data)
    except ValidationError:
        # Full semantic validation happens elsewhere; keep this permissive enough
        # to allow diagnostics on partially edited files.
        pass
    return data


def save_design(path: Path, data: dict[str, Any]) -> None:
    write_yaml(path, data)


def workspace_for_design_file(file: Path | None = None) -> Path:
    path = resolve_design_file(file)
    return path.parent


def suggestions_dir(file: Path | None = None) -> Path:
    ws = workspace_for_design_file(file)
    path = ws / "suggestions"
    path.mkdir(parents=True, exist_ok=True)
    return path


def outputs_dir(file: Path | None = None) -> Path:
    ws = workspace_for_design_file(file)
    path = ws / "outputs"
    path.mkdir(parents=True, exist_ok=True)
    return path
