import click
from pathlib import Path

NOTES_DIR = Path.home() / ".brain"
NOTES_DIR.mkdir(exist_ok=True)


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = NOTES_DIR / f"{name}.md"
    path.touch()
    click.echo(f"Added entry: {name}")
