import click

import logic

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
@click.pass_context
def brain(ctx):
    """Your brain in your terminal"""
    if ctx.invoked_subcommand is not None:
        logic.ensure_notes_dir()


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
