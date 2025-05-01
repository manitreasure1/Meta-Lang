import typer
import yaml
import os

from rich.console import Console

console = Console()
app = typer.Typer()

@app.command()
def create():
    """Initialize a new language"""

    console.print("[bold blue] MetaLang: Create your own language![/bold blue]")
    while True:
        name:str = typer.prompt("What is the name of your language?", default='', show_default=False)
        if not name.strip():
            console.print("[bold red]Error:[/] Name must not be empty.")
            continue
        console.print(f"[green] Name:[/] {name}")
        
        while True:
            extension: str = typer.prompt("What file extension should your language use? (e.g., .jj)", default='', show_default=False)
            if not extension.startswith("."):
                console.print("[bold red] Error:[/] Extension must start with a dot (e.g., .jj)")
                continue
            break

        filename = f"{name.lower().replace(' ', '_')}.yml"
        filepath = os.path.join("languages", filename)

        if os.path.exists(filepath):
            console.print(f"[bold yellow]⚠ Warning:[/] File '{filename}' already exists.")
            overwrite = typer.confirm("Do you want to overwrite it?", default=False)
            if not overwrite:
                console.print("[bold green]Continuing with the existing file.[/]")
                return

        config = {
            "name": name,
            "extension": extension,
            'syntax' : {
                "ml1": "print",
                "ml2": "input",
                "ml3": "return",
                "ml4": "if",
                "ml5": "else",
                "ml6": "elif",
                "ml7": "def",
                "ml8": "for",
                "ml9": "while",
                "ml10": "break",
                "ml11": "continue",
                "ml12": "import",
                "ml13": "from",
                "ml14": "as",
                "ml15": "pass",
                "ml16": "class",
                "ml17": "lambda",
                "ml18": "try",
                "ml19": "except",
                "ml20": "finally",
                "ml21": "raise",
                "ml22": "assert",
                "ml23": "with",
                "ml24": "yield",
                "ml25": "del",
                "ml26": "global",
                "ml27": "nonlocal",
                "ml28": "True",
                "ml29": "False",
                "ml30": "None",
                "ml31": "and",
                "ml32": "or",
                "ml33": "not",
                "ml34": "in",
                "ml35": "is",
                "ml36": "not in",
                "ml37": "is not",
                "ml38": "len",
                "ml39": "type",
                "ml40": "str",
                "ml41": "int",
                "ml42": "float",
                "ml43": "bool",
                "ml44": "list",
                "ml45": "dict",
                "ml46": "set",
                "ml47": "tuple",
                "ml48": "open",
                "ml49": "range",
                "ml50": "sum",
                "ml51": "min",
                "ml52": "max",
                "ml53": "abs",
                "ml54": "round",
                "ml55": "enumerate",
                "ml56": "zip",
                "ml57": "map",
                "ml58": "filter",
                "ml59": "any",
                "ml60": "all",
                "ml61": "sorted",
                "ml62": "reversed",
                "ml63": "help",
                "ml64": "id",
                "ml65": "dir",
                "ml66": "eval",
                "ml67": "exec",
                "ml68": "super",
                "ml69": "next",
                "ml70": "format",
            }
        }

        os.makedirs("languages", exist_ok=True)
        with open(filepath, "w") as f:
            yaml.dump(config, f, sort_keys=False)

        console.print(f"[green] Language '{name}' created in: [bold]languages/{filename}[/][/]")
        break
