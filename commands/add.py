import click
import subprocess
from config import get_brain_data_dir, TEXT_EDITOR

FILES_DIR = get_brain_data_dir()


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = FILES_DIR / f"{name}.md"
    path.touch()
    subprocess.run([TEXT_EDITOR, str(path)])
