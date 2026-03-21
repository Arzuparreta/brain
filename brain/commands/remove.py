import click

from brain.logic import note_path


@click.command(name="remove")
@click.argument("name")
def remove_files(name):
    """Delete something from your brain"""
    path = note_path(name)
    if path.exists():
        path.unlink()
        click.echo(f"{name} was deleted.")
    else:
        click.echo(f"Nothing named '{name}' found")
