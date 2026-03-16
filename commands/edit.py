import click
import subprocess
from config import TEXT_EDITOR
from logic import get_brain_data_dir

FILES_DIR = get_brain_data_dir()


@click.command(name="edit")
@click.argument("name", required=False)
def edit_files(name):
    """Edit the brain data files."""
    file_path = FILES_DIR
    if name:
        file_path = FILES_DIR / f"{name}.md"
    if file_path.exists():
        try:
            subprocess.run(TEXT_EDITOR.split() + [str(file_path)], check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Error opening editor: {e}")
    else:
        file_path = FILES_DIR
        try:
            subprocess.run(TEXT_EDITOR.split() + [str(file_path)])
        except subprocess.CalledProcessError as e:
            click.echo(f"Error opening editor: {e}")
