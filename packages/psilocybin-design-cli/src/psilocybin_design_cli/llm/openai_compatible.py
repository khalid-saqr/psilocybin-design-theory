from __future__ import annotations

import httpx

from psilocybin_design_cli.llm.guardrails import parse_and_validate_json


class OpenAICompatibleClient:
    def __init__(
        self,
        *,
        base_url: str,
        model: str,
        api_key: str = "local",
        temperature: float = 0.2,
        top_p: float = 0.8,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
        self.top_p = top_p

    def complete_json(self, prompt: str, *, schema_name: str = "llm-suggestion.schema.json") -> dict:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature,
            "top_p": self.top_p,
            "response_format": {"type": "json_object"},
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = httpx.post(f"{self.base_url}/chat/completions", json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        data = response.json()
        raw = data["choices"][0]["message"]["content"]
        return parse_and_validate_json(raw, schema_name=schema_name)
