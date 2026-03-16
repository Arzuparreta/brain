import click
from commands import add, list, remove, rename, edit, edit


@click.group()
def brain():
    """Your brain in your terminal"""
    pass


# Attatched commands
brain.add_command(add.add_files)
brain.add_command(list.list_files)
brain.add_command(remove.remove_files)
brain.add_command(rename.rename_files)
brain.add_command(edit.edit_files)

if __name__ == "__main__":
    brain()
