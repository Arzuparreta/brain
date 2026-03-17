import click

import os

from logic import dir


@click.command(name="rename")
@click.argument("old_name")
@click.argument("new_name")
def rename_files(old_name, new_name):
    """Rename something from your brain."""
    old_path = dir / f"{old_name}.md"
    new_path = dir / f"{new_name}.md"
    try:
        os.rename(old_path, new_path)
    except Exception:
        pass
    # Check
    if os.path.exists(new_path):
        print(f"File renamed to {new_name}.md")
    else:
        print("Failed to rename file.")
