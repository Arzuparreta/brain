import os

import click

from completion import get_completion_script

SENTINEL = os.path.expanduser("~/.config/brain/completion_installed")

SHELL_PATHS = {
    "fish": ("~/.config/fish/completions/brain.fish", None),
    "bash": ("~/.brain-complete.bash", "~/.bashrc"),
    "zsh": ("~/.brain-complete.zsh", "~/.zshrc"),
}


def _detect_shell():
    shell = os.environ.get("SHELL", "")
    for name in SHELL_PATHS:
        if name in shell:
            return name
    return None


def do_install(cli):
    shell = _detect_shell()
    if not shell:
        return False, "Could not detect shell from $SHELL. Supported: fish, bash, zsh."

    script = get_completion_script(cli, shell)
    if not script:
        return False, "Failed to generate completion script."

    dest = os.path.expanduser(SHELL_PATHS[shell][0])
    rc_file = SHELL_PATHS[shell][1]

    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as f:
        f.write(script)

    if rc_file:
        line = f"[ -f {dest} ] && . {dest}"
        return True, f"Completion installed to {dest}.\nAdd this to your {rc_file}:\n  {line}"
    return True, f"Completion installed to {dest}. Restart your shell."


def already_installed():
    return os.path.isfile(SENTINEL)


def mark_installed():
    os.makedirs(os.path.dirname(SENTINEL), exist_ok=True)
    open(SENTINEL, "a").close()


@click.command(name="install-completion")
@click.pass_context
def install_completion(ctx):
    """Install shell completions for brain."""
    ok, msg = do_install(ctx.find_root().command)
    click.echo(msg, err=not ok)
    if ok:
        mark_installed()
    else:
        raise SystemExit(1)
