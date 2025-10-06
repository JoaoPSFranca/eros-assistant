from typer.testing import CliRunner


def test_main_command_prints_greeting_and_exits(monkeypatch, mocker):
    monkeypatch.setenv("GEMINI_API_KEY", "test_key_for_main")

    mocker.patch("eros.main.brain.initialize_brain", return_value=None)

    from eros.main import app

    runner = CliRunner()

    result = runner.invoke(app, input="sair\n")

    assert result.exit_code == 0
    assert "Olá! Eu sou Eros." in result.stdout
    assert "Até logo!" in result.stdout
