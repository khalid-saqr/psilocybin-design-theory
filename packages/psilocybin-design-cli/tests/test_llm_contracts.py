from pathlib import Path
import json
import pytest
from psilocybin_design_cli.llm.guardrails import validate_suggestion_contract
from psilocybin_design_cli.errors import LLMError

FIX = Path(__file__).parent / "fixtures"


def test_valid_llm_suggestion_passes():
    data = json.loads((FIX / "valid_llm_suggestion.json").read_text())
    validate_suggestion_contract(data)


def test_suggestion_without_evidence_fails():
    data = json.loads((FIX / "valid_llm_suggestion.json").read_text())
    data["suggestions"][0]["evidence"] = []
    with pytest.raises(LLMError):
        validate_suggestion_contract(data)


def test_unknown_target_path_fails():
    data = json.loads((FIX / "valid_llm_suggestion.json").read_text())
    data["suggestions"][0]["target_path"] = "filesystem"
    with pytest.raises(LLMError):
        validate_suggestion_contract(data)
