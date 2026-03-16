from config import FILES_DIR
import click


@click.command(hidden=True, name="complete_edit")
def complete_edit():
    """Return filenames for fish completion"""
    for f in FILES_DIR.glob("*.md"):
        print(f.stem)
