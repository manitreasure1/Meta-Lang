import os
import typer
import yaml
from metalang.utils.parser import parser
from rich.console import Console


console = Console()



def check_file(filename: str, yml_name: str):
    yml_path = os.path.join("languages", yml_name)

    # Check if files exist
    if not os.path.exists(filename):
        console.print(f"[red][Error][/] Source file '{filename}' does not exist.")
        raise typer.Exit(1)
    if not os.path.exists(yml_path):
        console.print(f"[red][Error][/] YAML file '{yml_path}' does not exist.")
        raise typer.Exit(1)

    # Check extension matches yml config
    with open(yml_path, 'r') as f:
        config = yaml.safe_load(f)
    expected_ext = config.get('extension', None)
    if not expected_ext:
        console.print("[red][Error][/] No 'extension' field found in YAML config.")
        raise typer.Exit(1)
    if not filename.endswith(expected_ext):
        console.print(f"[red][Error][/] File extension does not match YAML config. Expected '{expected_ext}'.")
        raise typer.Exit(1)

    # Transpile to Python
    python_code = parser(filename, yml_path)
    return python_code
    