from rich.progress import track
from rich.console import Console
import time
import typer
import os


app = typer.Typer()
console = Console()


@app.command()
def publish(zip_filename: str):
    """Pulish Language to MetaLang Hub"""

    if not zip_filename.endswith('zip'):
        console.print(f"[red]{zip_filename} is not a zipfile[/]")
        raise typer.Exit(1)
        
    if not os.path.exists(zip_filename):
        console.print(f"[red]{zip_filename} not found build project zip file to continue[/]")
        raise typer.Exit(1)

    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
        upload_to_hub(zip_filename)
    console.print(f"Processed {total} things.")


def upload_to_hub(zip_filename):
    """publish logic"""
    ...