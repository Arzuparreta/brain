import subprocess

import click

from logic import note_path, open_in_editor
from settings import settings


@click.command(name="add")
@click.argument("name")
def add_files(name):
    """Stick something to your brain"""
    path = note_path(name)
    try:
        open_in_editor(path, check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error opening {settings['TEXT_EDITOR']}: {e}")
