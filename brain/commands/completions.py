import click

from brain.logic import notes_dir
from brain.settings import settings


@click.command(hidden=True, name="complete_files")
def complete_files():
    """Return filenames for fish completion."""
    pattern = f"*.{settings['NOTE_EXTENSION']}"
    for f in notes_dir().glob(pattern):
        print(f.stem)
