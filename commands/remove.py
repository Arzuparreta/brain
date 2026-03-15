import click
from pathlib import Path
from config import get_brain_data_dir

NOTES_DIR = get_brain_data_dir()


@click.command(name="remove")
@click.argument("name")
def remove_files(name):
    """Delete something from your brain"""
    path = NOTES_DIR / f"{name}.md"
    if path.exists():
        path.unlink()
        click.echo(f"{name} was deleted.")
    else:
        click.echo(f"Nothing named '{name}' found")
