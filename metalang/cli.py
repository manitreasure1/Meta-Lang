import typer
from metalang.commands import init

app = typer.Typer()

app.add_typer(init.app)

if __name__ == "__main__":
    app()
