from pathlib import Path
from psilocybin_design_cli.io import read_yaml
from psilocybin_design_cli.core.validate import validate_design

FIX = Path(__file__).parent / "fixtures"


def test_relation_to_unknown_verb_fails():
    data = read_yaml(FIX / "valid_design.yaml")
    data["relations"][0]["traces_to_verbs"] = ["verb-nope"]
    report = validate_design(data)
    assert not report.ok


def test_invariant_to_unknown_relation_fails():
    data = read_yaml(FIX / "valid_design.yaml")
    data["invariants"][0]["traces_to_relations"] = ["relation-nope"]
    report = validate_design(data)
    assert not report.ok


def test_implementation_phase_with_no_trace_fails():
    data = read_yaml(FIX / "valid_design.yaml")
    data["implementation_sequence"][0]["traces_to"] = []
    report = validate_design(data)
    assert not report.ok
