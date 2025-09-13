import typer

app = typer.Typer(
    name="Eros",
    help="Um assistente virtual pessoal para automação e auxílio no desenvolvimento.",
    add_completion=False,
)

@app.command()
def main():
    """
    Ponto de entrada principal para a assistente Eros.
    """
    typer.secho("Olá! Eu sou Eros. Atualmente em desenvolvimento.", fg=typer.colors.CYAN)

if __name__ == "__main__":
    app()