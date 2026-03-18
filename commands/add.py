import click

import subprocess

from logic import editor, extension, dir


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = dir / f"{name}.{extension}"
    try:
        subprocess.run([editor, str(path)])
    except subprocess.CalledProcessError as e:
        click.echo(f"Error opening f{editor}: {e}")
