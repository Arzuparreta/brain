import click

from logic import dir


@click.command(hidden=True, name="complete_files")
def complete_files():
    """Return filenames for fish completion"""
    for f in dir.glob("*.md"):
        print(f.stem)
