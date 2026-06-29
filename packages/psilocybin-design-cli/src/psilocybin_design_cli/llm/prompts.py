from __future__ import annotations

import json
from importlib.resources import files

from psilocybin_design_cli.constants import CONTROLLED_VERBS

PACKAGE = "psilocybin_design_cli"

BASE_GUARDRAILS = """You are assisting Psilocybin Genesis CLI.

You must:
- Use only the provided user material.
- Do not invent facts.
- Return only valid JSON.
- Every suggestion must cite evidence from the provided material.
- Do not decide final design authority.
- Do not generate implementation code.
- Do not bypass schema requirements.
"""


def load_prompt_template(stage: str) -> str:
    name = f"suggest_{stage}.txt"
    path = files(PACKAGE) / "templates" / "prompts" / name
    if not path.exists():
        path = files(PACKAGE) / "templates" / "prompts" / "suggest_sequence.txt"
    return path.read_text(encoding="utf-8")


def build_prompt(stage: str, design: dict) -> str:
    template = load_prompt_template(stage)
    payload = json.dumps(design, ensure_ascii=False, indent=2)
    return (
        BASE_GUARDRAILS
        + "\nControlled hidden verbs: "
        + ", ".join(CONTROLLED_VERBS)
        + "\n\n"
        + template
        + "\n\nCurrent design memory JSON:\n"
        + payload
    )
