from typer.testing import CliRunner
from psilocybin_design_cli.cli import app

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Psilocybin" in result.output or "psilocybin" in result.output
