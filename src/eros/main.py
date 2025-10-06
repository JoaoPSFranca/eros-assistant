import rich
import typer
from dotenv import load_dotenv

from eros import brain
from eros.config import Settings

load_dotenv()

try:
    settings = Settings()
    brain.initialize_brain(api_key=settings.GEMINI_API_KEY)
except (ValueError, RuntimeError) as e:
    typer.secho(f"Erro de inicialização: {e}", fg=typer.colors.RED)
    raise typer.Exit(code=1)

app = typer.Typer(
    name="Eros",
    help="Um assistente virtual pessoal para automação e auxílio no desenvolvimento.",
    add_completion=False,
)


@app.command()
def main():
    typer.secho(
        "Olá! Eu sou Eros. Digite 'sair' ou 'exit' para terminar.", fg=typer.colors.CYAN
    )

    chat_session = brain.start_chat_session()

    while True:
        prompt = typer.prompt("Você")
        if prompt.lower() in ["sair", "exit"]:
            typer.secho("Até logo!", fg=typer.colors.CYAN)
            break

        with rich.get_console().status(
            "[bold green]Eros está pensando...", spinner="dots"
        ):
            response = brain.get_chat_response(chat_session, prompt)

        rich.print(f"[bold cyan]Eros:[/bold cyan] {response}")


if __name__ == "__main__":
    app()
