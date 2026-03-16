from click.shell_completion import BashComplete, FishComplete, ZshComplete

from config import get_brain_file_stems

SHELLS = {"fish": FishComplete, "bash": BashComplete, "zsh": ZshComplete}


def complete_brain_names(ctx, param, incomplete):
    return [s for s in get_brain_file_stems() if s.startswith(incomplete)]


def get_completion_script(cli, shell):
    """Use Click's API directly — no subprocess, no env var guessing."""
    cls = SHELLS.get(shell)
    if not cls:
        return None
    return cls(cli, {}, "brain", "_BRAIN_COMPLETE").source()
