import os
import click
from config import FILES_DIR
from completion import complete_brain_names


@click.command(name="rename")
@click.argument("old_name", shell_complete=complete_brain_names)
@click.argument("new_name", shell_complete=complete_brain_names)
def rename_files(old_name, new_name):
    """Rename something from your brain."""
    old_path = FILES_DIR / f"{old_name}.md"
    new_path = FILES_DIR / f"{new_name}.md"
    try:
        os.rename(old_path, new_path)
    except Exception:
        pass
    # Check
    if os.path.exists(new_path):
        print(f"File renamed to {new_name}.md")
    else:
        print("Failed to rename file.")
