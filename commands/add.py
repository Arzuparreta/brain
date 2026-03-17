import click
import subprocess
from settings import settings
from logic import get_brain_data_dir

FILES_DIR = get_brain_data_dir()
editor = settings["TEXT_EDITOR"]
extension = settings["NOTE_EXTENSION"]


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = FILES_DIR / f"{name}.{extension}"
    try:
        subprocess.run([editor, str(path)])
    except subprocess.CalledProcessError as e:
        click.echo(f"Error opening f{editor}: {e}")
