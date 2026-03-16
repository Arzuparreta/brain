import click
from logic import get_brain_data_dir

FILES_DIR = get_brain_data_dir()


@click.command(name="list")
def list_files():
    """List your brain files"""
    files = [f.name for f in FILES_DIR.iterdir() if f.is_file()]
    if not files:
        click.echo("Your brain is empty.")
    else:
        click.echo("Your brain:")
        for file in files:
            click.echo(f"- {file}")
