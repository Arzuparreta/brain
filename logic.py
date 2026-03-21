import shlex
import subprocess
from pathlib import Path

from settings import settings


def notes_dir() -> Path:
    root = settings["FILES_DIR"]
    return root if isinstance(root, Path) else Path(root)


def note_path(stem: str) -> Path:
    ext = settings["NOTE_EXTENSION"]
    return notes_dir() / f"{stem}.{ext}"


def ensure_notes_dir() -> Path:
    d = notes_dir()
    d.mkdir(parents=True, exist_ok=True)
    return d


def editor_argv() -> list[str]:
    return shlex.split(settings["TEXT_EDITOR"])


def open_in_editor(path: Path, *, check: bool) -> None:
    argv = editor_argv() + [str(path)]
    subprocess.run(argv, check=check)
