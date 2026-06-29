from typer.testing import CliRunner
from psilocybin_design_cli.cli import app

runner = CliRunner()


def test_init_creates_workspace(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["init", "demo", "--no-llm"])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "demo.design" / "psilocybin.design.yaml").exists()


def test_init_refuses_overwrite(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert runner.invoke(app, ["init", "demo"]).exit_code == 0
    result = runner.invoke(app, ["init", "demo"])
    assert result.exit_code != 0
