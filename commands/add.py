import click
import subprocess
from config import TEXT_EDITOR
from logic import get_brain_data_dir

FILES_DIR = get_brain_data_dir()


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = FILES_DIR / f"{name}.md"
    try:
        subprocess.run([TEXT_EDITOR, str(path)])
    except subprocess.CalledProcessError as e:
        click.echo(f"Error opening f{TEXT_EDITOR}: {e}")
