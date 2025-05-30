from rich.progress import track
import time
import typer
from metalang.utils.file_checker import check_file


app = typer.Typer()


@app.command()
def publish(filename: str, yml_name: str):
    """Pulish Language to MetaLang Hub"""

    python_file = check_file(filename, yml_name)

    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")
