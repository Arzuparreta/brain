import click
from config import get_brain_data_dir
from completion import complete_brain_names

FILES_DIR = get_brain_data_dir()


@click.command(name="remove")
@click.argument("name", shell_complete=complete_brain_names)
def remove_files(name):
    """Delete something from your brain"""
    path = FILES_DIR / f"{name}.md"
    if path.exists():
        path.unlink()
        click.echo(f"{name} was deleted.")
    else:
        click.echo(f"Nothing named '{name}' found")
