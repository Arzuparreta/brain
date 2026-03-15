import click
from config import get_brain_data_dir

NOTES_DIR = get_brain_data_dir()


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = NOTES_DIR / f"{name}.md"
    path.touch()
    click.echo(f"Added entry: {name}")
