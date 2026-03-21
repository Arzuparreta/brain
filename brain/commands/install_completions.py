import pathlib

import click

from brain.constants import FISH_SUBCOMMANDS


@click.command(name="install_completions")
def install_completions():
    """Install Fish completions under ~/.config (not portable; prefer repo brain.fish)."""
    subcommands = " ".join(FISH_SUBCOMMANDS)
    completion = f"""
function __brain_complete_files
    brain complete_files
end

complete -c brain -f
complete -c brain -n "__fish_use_subcommand" -a "{subcommands}"
complete -c brain -n "__fish_seen_subcommand_from edit remove see" -a "(__brain_complete_files)"
complete -c brain -n "__fish_seen_subcommand_from rename" -a "(__brain_complete_files)"
"""

    path = pathlib.Path.home() / ".config/fish/completions/brain.fish"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(completion.lstrip())

    click.echo(f"Installed fish completion at {path}")
