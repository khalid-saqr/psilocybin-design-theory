from __future__ import annotations

import json
from typing import Any

from psilocybin_design_cli.constants import ALLOWED_TARGET_PATHS, LLM_STAGES
from psilocybin_design_cli.core.schema import validate_with_schema
from psilocybin_design_cli.errors import LLMError


def extract_json(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    try:
        data = json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise LLMError(f"LLM output was not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise LLMError("LLM output JSON must be an object.")
    return data


def validate_suggestion_contract(data: dict[str, Any], *, schema_name: str = "llm-suggestion.schema.json") -> None:
    schema_errors = validate_with_schema(data, schema_name)
    if schema_errors:
        raise LLMError("LLM suggestion schema errors: " + "; ".join(schema_errors))
    stage = data.get("stage")
    if stage not in LLM_STAGES:
        raise LLMError(f"Unknown LLM suggestion stage: {stage}")
    for suggestion in data.get("suggestions", []):
        target = suggestion.get("target_path")
        if target not in ALLOWED_TARGET_PATHS:
            raise LLMError(f"Suggestion target_path is not allowlisted: {target}")
        if not suggestion.get("evidence"):
            raise LLMError(f"Suggestion lacks evidence: {suggestion.get('id')}")
        if not suggestion.get("reason"):
            raise LLMError(f"Suggestion lacks reason: {suggestion.get('id')}")


def parse_and_validate_json(text: str, *, schema_name: str = "llm-suggestion.schema.json") -> dict[str, Any]:
    data = extract_json(text)
    validate_suggestion_contract(data, schema_name=schema_name)
    return data
