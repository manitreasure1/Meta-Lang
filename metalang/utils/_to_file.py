import os
import zipfile
from rich.console import Console


console = Console()


def generate_python_file(filename: str, python_code: str) -> None:
    
    py_filename = os.path.splitext(filename)[0] + '.py'
    with open(py_filename, 'w', encoding='utf-8') as f:
        f.write(python_code)
    console.print(f"\n[green][Build] Transpiled[/] '{filename}' to '{py_filename}'")
    
    try:
        compile(python_code, py_filename, 'exec')
        console.print("[green][Analysis] No syntax errors detected.")
    except SyntaxError as e:
        console.print(f"[red][red][Analysis][/] Syntax error: {e}")



def generate_zip_file(filename:str):
    # Bundle (zip) the source and generated files
    bundle_name = os.path.splitext(filename)[0] + '_bundle.zip'
    with zipfile.ZipFile(bundle_name, 'w') as bundle:
        bundle.write(filename)
    console.print(f"[green][Bundle][/] Project files bundled as '{bundle_name}'.")

