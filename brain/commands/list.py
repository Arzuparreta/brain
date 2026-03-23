import click

from brain.logic import notes_dir


@click.command(name="list")
def list_files():
    """List your brain files."""
    files = [f.name for f in notes_dir().iterdir() if f.is_file()]
    if not files:
        click.echo("Your brain is empty.")
    else:
        click.echo("Your brain:")
        for file in files:
            click.echo(f"- {file}")
