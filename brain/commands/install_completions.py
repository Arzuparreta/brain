import pathlib

import click

from brain.constants import FISH_SUBCOMMANDS
from brain.paths import brain_root


@click.command(name="install_completions")
def install_completions():
    """Write Fish completions to ~/.config/fish/completions/."""
    brain_exec = brain_root() / "bin" / "brain"
    q = str(brain_exec).replace("'", "'\\''")
    subcommands = " ".join(FISH_SUBCOMMANDS)
    completion = f"""# brain-cli-completions (managed by brain/scripts/setup.sh — do not edit by hand)
function __brain_complete_files
    command '{q}' complete_files
end

complete -c brain -f
complete -c brain -n "__fish_use_subcommand" -a "{subcommands}"
complete -c brain -n "__fish_seen_subcommand_from edit remove see" -a "(__brain_complete_files)"
complete -c brain -n "__fish_seen_subcommand_from rename" -a "(__brain_complete_files)"
"""

    path = pathlib.Path.home() / ".config/fish/completions/brain.fish"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(completion)

    click.echo(f"Installed fish completion at {path}")
