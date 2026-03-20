from settings import settings

import click

from commands import (
    add,
    list,
    remove,
    rename,
    edit,
    see,
    install_completions,
    completions,
)


@click.group()
def brain():
    """Your brain in your terminal"""


# Attatched commands
brain.add_command(add.add_files)
brain.add_command(list.list_files)
brain.add_command(remove.remove_files)
brain.add_command(rename.rename_files)
brain.add_command(edit.edit_files)
brain.add_command(see.see_files)
brain.add_command(install_completions.install_completions)
brain.add_command(completions.complete_files)

if __name__ == "__main__":
    brain()
