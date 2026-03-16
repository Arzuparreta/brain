import click
import subprocess
from config import get_brain_data_dir, TEXT_EDITOR
from completion import complete_brain_names

FILES_DIR = get_brain_data_dir()


@click.command(name="add")
@click.argument("name", shell_complete=complete_brain_names)
def add_files(name):
    """Stick something to your brain"""
    path = FILES_DIR / f"{name}.md"
    subprocess.run([TEXT_EDITOR, str(path)])
