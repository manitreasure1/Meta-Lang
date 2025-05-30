import typer
from rich.console import Console
from metalang.utils.file_checker import check_file


console = Console()
app = typer.Typer()


@app.command()
def run(filename: str, yml_name: str):
    """Run the Design Language"""
    
    python_code = check_file(filename, yml_name)
    try:
        exec(python_code, {})
    except Exception as e:
        console.print(f"[red][Runtime Error][/] {e}")


