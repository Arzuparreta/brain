from config import FILES_DIR
import click


@click.command(hidden=True, name="complete_files")
def complete_files():
    """Return filenames for fish completion"""
    for f in FILES_DIR.glob("*.md"):
        print(f.stem)
