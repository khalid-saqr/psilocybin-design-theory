from pathlib import Path
from psilocybin_design_cli.io import read_yaml
from psilocybin_design_cli.core.schema import validate_with_schema

FIX = Path(__file__).parent / "fixtures"


def test_valid_fixture_passes_schema():
    data = read_yaml(FIX / "valid_design.yaml")
    assert validate_with_schema(data, "psilocybin-design.schema.json") == []


def test_invalid_schema_version_fails():
    data = read_yaml(FIX / "valid_design.yaml")
    data["schema_version"] = "9"
    assert validate_with_schema(data, "psilocybin-design.schema.json")
