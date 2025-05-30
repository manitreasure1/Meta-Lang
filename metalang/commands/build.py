
import re
import typer
from metalang.utils.file_checker import check_file
from metalang.utils._to_file import generate_python_file, generate_zip_file
from rich.progress import track


app = typer.Typer()


@app.command()
def build(filename: str, yml_name: str):
    """Transpile a custom language file to Python, analyze, and generate documentation."""
    
    steps = [
        ("Checking files and transpiling", lambda: check_file(filename, yml_name)),
        ("Generating Python file", lambda python_code: generate_python_file(filename, python_code)),
        ("Bundling project files", lambda _: generate_zip_file(filename)),
        ("Generating documentation", None),
    ]

    python_code = None
    for description, action in track(steps, description="[cyan]Building project...[/]"):
        if description == "Checking files and transpiling":
            python_code = action()
        elif description == "Generating Python file":
            if python_code is not None:
                action(python_code)
        elif description == "Bundling project files":
            action(None)
        elif description == "Generating documentation":
            ...

    
    if python_code is not None:
        functions = re.findall(r'def (\w+)\(', python_code)
        classes = re.findall(r'class (\w+)\(', python_code)
        if functions or classes:
            typer.echo("[Docs] F/C found:")
            for func in functions:
                typer.echo(f"  - {func}()")
            for cls in classes:
                typer.echo(f"  - {cls}()")
        else:
            typer.echo("[Docs] No functions or classes found.")
    else:
        typer.echo("[Docs] No Python code generated, skipping documentation.")


