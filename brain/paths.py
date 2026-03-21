import os
from pathlib import Path


def brain_root() -> Path:
    """Repository / portable app root (parent of the `brain` package)."""
    env = os.environ.get("BRAIN_ROOT")
    if env:
        return Path(env).resolve()
    return Path(__file__).resolve().parent.parent
