from typer.testing import CliRunner
from eros.main import app

runner = CliRunner()

def test_main_command_prints_greeting():
    """
    Testa se o comando principal (sem subcomandos) é executado com sucesso
    e imprime a mensagem de saudação esperada.
    """
    result = runner.invoke(app)

    assert result.exit_code == 0

    assert "Olá! Eu sou Eros." in result.stdout
