import click


@click.command(name="install_completions")
def install_completions():
    import pathlib

    completion = """
function __brain_complete_files
    brain complete_files
end

complete -c brain -f
complete -c brain -n "__fish_use_subcommand" -a "edit add list remove"
complete -c brain -n "__fish_seen_subcommand_from edit remove" -a "(__brain_complete_files)"
"""

    path = pathlib.Path.home() / ".config/fish/completions/brain.fish"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(completion)

    click.echo(f"Installed fish completion at {path}")
