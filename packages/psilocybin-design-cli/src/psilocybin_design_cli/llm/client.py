from __future__ import annotations

from typing import Protocol


class LLMClient(Protocol):
    def complete_json(self, prompt: str, *, schema_name: str = "llm-suggestion.schema.json") -> dict:
        ...
