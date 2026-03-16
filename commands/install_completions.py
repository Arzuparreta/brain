import click


@click.command(name="install_completions")
def install_completions():
    import pathlib

    completion = """
function __brain_complete_edit
    brain complete_edit
end

complete -c brain -f
complete -c brain -n "__fish_use_subcommand" -a "edit"
complete -c brain -n "__fish_seen_subcommand_from edit" -a "(__brain_complete_edit)"
"""

    path = pathlib.Path.home() / ".config/fish/completions/brain.fish"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(completion)

    click.echo(f"Installed fish completion at {path}")
