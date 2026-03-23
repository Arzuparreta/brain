import subprocess

from brain.logic import note_path, notes_dir, open_in_editor


def edit_files(name):
    """Edit the brain data files."""
    notes = notes_dir()
    if not name:
        target, check = notes, True
    else:
        candidate = note_path(name)
        if candidate.exists():
            target, check = candidate, True
        else:
            target, check = notes, False
    try:
        open_in_editor(target, check=check)
    except subprocess.CalledProcessError as e:
        print(f"Error opening editor: {e}")
