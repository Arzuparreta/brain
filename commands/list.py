import click
from pathlib import Path

NOTES_DIR = Path.home() / ".brain"


@click.command(name="list")
def list_files():
    """List your brain files"""
    notes = [f.name for f in NOTES_DIR.iterdir() if f.is_file()]
    if not notes:
        click.echo("Your brain is empty.")
    else:
        click.echo("Your notes:")
        for note in notes:
            click.echo(f"- {note}")
