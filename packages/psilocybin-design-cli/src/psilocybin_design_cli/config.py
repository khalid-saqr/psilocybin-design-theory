from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from platformdirs import user_config_dir

from .constants import APP_NAME
from .io import read_yaml, write_yaml

DEFAULT_CONFIG: dict[str, Any] = {
    "llm": {
        "enabled": False,
        "provider": "ollama",
        "model": "qwen3:4b",
        "base_url": "http://localhost:11434",
        "temperature": 0.2,
        "top_p": 0.8,
        "max_output_tokens": 2048,
        "require_json": True,
        "require_user_acceptance": True,
    }
}


def user_config_path() -> Path:
    return Path(user_config_dir(APP_NAME, appauthor=False)) / "config.yaml"


def workspace_config_path(workspace: Path | None) -> Path | None:
    if workspace is None:
        return None
    return workspace / ".psilocybin" / "config.yaml"


def deep_update(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_update(result[key], value)
        else:
            result[key] = value
    return result


def load_config(workspace: Path | None = None) -> dict[str, Any]:
    cfg = deepcopy(DEFAULT_CONFIG)
    upath = user_config_path()
    if upath.exists():
        cfg = deep_update(cfg, read_yaml(upath))
    wpath = workspace_config_path(workspace)
    if wpath and wpath.exists():
        cfg = deep_update(cfg, read_yaml(wpath))
    return cfg


def set_dotted(config: dict[str, Any], key: str, value: Any) -> None:
    parts = key.split(".")
    cur = config
    for part in parts[:-1]:
        cur = cur.setdefault(part, {})
    cur[parts[-1]] = coerce_value(value)


def get_dotted(config: dict[str, Any], key: str) -> Any:
    cur: Any = config
    for part in key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(key)
        cur = cur[part]
    return cur


def coerce_value(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    lower = value.lower()
    if lower == "true":
        return True
    if lower == "false":
        return False
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def save_workspace_config(workspace: Path, config: dict[str, Any]) -> None:
    path = workspace_config_path(workspace)
    assert path is not None
    write_yaml(path, config)


def save_user_config(config: dict[str, Any]) -> None:
    write_yaml(user_config_path(), config)
