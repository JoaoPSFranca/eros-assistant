import typer
from dotenv import load_dotenv

load_dotenv()

from eros.config import Settings

try:
    settings = Settings()
except ValueError as e:
    typer.secho(f"Erro de configuração: {e}", fg=typer.colors.RED)
    raise typer.Exit(code=1)

app = typer.Typer(
    name="Eros",
    help="Um assistente virtual pessoal para automação e auxílio no desenvolvimento.",
    add_completion=False,
)

@app.command()
def main():
    typer.secho("Olá! Eu sou Eros. Configuração carregada com sucesso.", fg=typer.colors.CYAN)

if __name__ == "__main__":
    app()