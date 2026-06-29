from pathlib import Path
from psilocybin_design_cli.io import read_yaml
from psilocybin_design_cli.core.render import render_genesis_repo

FIX = Path(__file__).parent / "fixtures"


def test_render_valid_design(tmp_path):
    out = tmp_path / "repo"
    render_genesis_repo(read_yaml(FIX / "valid_design.yaml"), out)
    assert (out / "AGENTS.md").exists()
    text = (out / "AGENTS.md").read_text()
    assert "Begin with `psilocybin.design.yaml`" in text
    assert "Compliance checklist" in text
