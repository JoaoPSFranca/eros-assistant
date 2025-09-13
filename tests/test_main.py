from typer.testing import CliRunner

def test_main_command_prints_greeting(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test_key_for_main")

    from eros.main import app

    runner = CliRunner()
    result = runner.invoke(app)

    assert result.exit_code == 0
    assert "Configuração carregada com sucesso" in result.stdout