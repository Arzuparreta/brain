import click

from logic import dir


@click.command(name="remove")
@click.argument("name")
def remove_files(name):
    """Delete something from your brain"""
    path = dir / f"{name}.md"
    if path.exists():
        path.unlink()
        click.echo(f"{name} was deleted.")
    else:
        click.echo(f"Nothing named '{name}' found")
