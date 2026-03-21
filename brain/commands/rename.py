import click

from brain.logic import note_path


@click.command(name="rename")
@click.argument("old_name")
@click.argument("new_name")
def rename_files(old_name, new_name):
    """Rename something from your brain."""
    old_path = note_path(old_name)
    new_path = note_path(new_name)
    ext = new_path.suffix
    try:
        old_path.rename(new_path)
    except FileNotFoundError:
        click.echo("Failed to rename file.")
        return
    except OSError:
        click.echo("Failed to rename file.")
        return
    click.echo(f"File renamed to {new_name}{ext}")
