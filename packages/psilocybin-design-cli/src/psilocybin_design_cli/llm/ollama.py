from __future__ import annotations

import httpx

from psilocybin_design_cli.llm.guardrails import parse_and_validate_json


class OllamaClient:
    def __init__(self, *, base_url: str, model: str, temperature: float = 0.2, top_p: float = 0.8):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.temperature = temperature
        self.top_p = top_p

    def complete_json(self, prompt: str, *, schema_name: str = "llm-suggestion.schema.json") -> dict:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": self.temperature, "top_p": self.top_p},
        }
        response = httpx.post(f"{self.base_url}/api/generate", json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        raw = data.get("response", "")
        return parse_and_validate_json(raw, schema_name=schema_name)

    def list_models(self) -> list[str]:
        response = httpx.get(f"{self.base_url}/api/tags", timeout=10)
        response.raise_for_status()
        data = response.json()
        return [m.get("name", "") for m in data.get("models", []) if m.get("name")]
