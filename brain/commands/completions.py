from brain.logic import notes_dir
from brain.settings import settings


def complete_files():
    """Return filenames for fish completion."""
    pattern = f"*.{settings['NOTE_EXTENSION']}"
    for f in notes_dir().glob(pattern):
        print(f.stem)
