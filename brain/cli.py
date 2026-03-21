import click

from brain import logic
from brain.commands import (
    add,
    completions,
    edit,
    install_completions,
    list,
    remove,
    rename,
    see,
)


@click.group()
@click.version_option(package_name="brain")
@click.pass_context
def cli(ctx):
    """Your brain in your terminal"""
    if ctx.invoked_subcommand is not None:
        logic.ensure_notes_dir()


cli.add_command(add.add_files)
cli.add_command(list.list_files)
cli.add_command(remove.remove_files)
cli.add_command(rename.rename_files)
cli.add_command(edit.edit_files)
cli.add_command(see.see_files)
cli.add_command(install_completions.install_completions)
cli.add_command(completions.complete_files)


def main():
    cli()
