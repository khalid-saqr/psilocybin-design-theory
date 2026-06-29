from __future__ import annotations

import json
from importlib.resources import files
from typing import Any

from jsonschema import Draft202012Validator

PACKAGE = "psilocybin_design_cli"


def load_schema(name: str) -> dict[str, Any]:
    text = (files(PACKAGE) / "schemas" / name).read_text(encoding="utf-8")
    return json.loads(text)


def validate_with_schema(data: dict[str, Any], schema_name: str) -> list[str]:
    schema = load_schema(schema_name)
    validator = Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        location = "/".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"{location}: {err.message}")
    return errors
