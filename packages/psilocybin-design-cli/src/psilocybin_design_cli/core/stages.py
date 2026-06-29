from __future__ import annotations

from psilocybin_design_cli.constants import STAGES, LLM_STAGES


def require_stage(stage: str, *, llm: bool = False) -> str:
    allowed = LLM_STAGES if llm else STAGES
    if stage not in allowed:
        raise ValueError(f"Unknown stage '{stage}'. Expected one of: {', '.join(allowed)}")
    return stage
