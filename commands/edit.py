import click
import subprocess
from config import TEXT_EDITOR
from logic import get_brain_data_dir

FILES_DIR = get_brain_data_dir()


@click.command(name="edit")
def edit_files():
    """Edit the brain data files."""
    try:
        subprocess.run([TEXT_EDITOR, FILES_DIR], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error opening editor: {e}")
