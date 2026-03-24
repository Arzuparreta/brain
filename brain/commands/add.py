import subprocess

from brain.logic import note_path, open_in_editor
from brain.settings import settings


def add_files(name):
    """Stick something to your brain."""
    path = note_path(name)
    try:
        open_in_editor(path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error opening {settings['TEXT_EDITOR']}: {e}")
