import click
from config import get_brain_data_dir

NOTES_DIR = get_brain_data_dir()


@click.command(name="list")
def list_files():
    """List your brain files"""
    notes = [f.name for f in NOTES_DIR.iterdir() if f.is_file()]
    if not notes:
        click.echo("Your brain is empty.")
    else:
        click.echo("Your brain:")
        for note in notes:
            click.echo(f"- {note}")
