import click

from brain.logic import note_path


@click.command(name="see")
@click.argument("name")
def see_files(name):
    path = note_path(name)
    try:
        click.echo(path.read_text())
    except FileNotFoundError:
        click.echo("File not found.")
    except PermissionError:
        click.echo("You don't have permission to read this file")
