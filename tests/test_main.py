from typer.testing import CliRunner

from typer_demo.main import app

runner = CliRunner()


def test_main_shoot():
    result = runner.invoke(app, ["shoot"])
    assert result.exit_code == 0
    assert "pyum pyum" in result.stdout


def test_main_load():
    result = runner.invoke(app, ["load"])
    assert result.exit_code == 0
    assert "Recargar portal!" in result.stdout
