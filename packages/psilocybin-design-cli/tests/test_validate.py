from pathlib import Path
from psilocybin_design_cli.io import read_yaml
from psilocybin_design_cli.core.validate import validate_design

FIX = Path(__file__).parent / "fixtures"


def test_valid_design_has_no_errors():
    report = validate_design(read_yaml(FIX / "valid_design.yaml"))
    assert report.ok, [m.message for m in report.errors]


def test_missing_genome_with_stack_fails():
    report = validate_design(read_yaml(FIX / "invalid_missing_genome.yaml"))
    assert not report.ok
    assert any(m.name == "stack.trace_to_genome" for m in report.errors)


def test_untraced_stack_fails():
    report = validate_design(read_yaml(FIX / "invalid_untraced_stack.yaml"))
    assert not report.ok
    assert any(m.name == "stack.trace_to_survival" for m in report.errors)
