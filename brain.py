import click
from commands import add, install_completion, list, remove, rename


@click.group()
@click.pass_context
def brain(ctx):
    """Your brain in your terminal"""
    if not ctx.invoked_subcommand or ctx.invoked_subcommand == "install-completion":
        return
    if install_completion.already_installed():
        return
    click.echo("Install shell completions for brain? [y/N] ", nl=False)
    try:
        ans = input().strip().lower()
    except (EOFError, KeyboardInterrupt):
        return
    if ans in ("y", "yes"):
        ok, msg = install_completion.do_install(ctx.command)
        click.echo(msg)
        if ok:
            install_completion.mark_installed()


brain.add_command(add.add_files)
brain.add_command(list.list_files)
brain.add_command(remove.remove_files)
brain.add_command(rename.rename_files)
brain.add_command(install_completion.install_completion)

if __name__ == "__main__":
    brain()
