import typer
from metalang.commands import init, publish, run, build

app = typer.Typer()

app.add_typer(init.app)
app.add_typer(publish.app)
app.add_typer(run.app)
app.add_typer(build.app)

if __name__ == "__main__":
    app()
