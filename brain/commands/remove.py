from brain.logic import note_path


def remove_files(name):
    """Delete something from your brain."""
    path = note_path(name)
    if path.exists():
        path.unlink()
        print(f"{name} was deleted.")
    else:
        print(f"Nothing named '{name}' found")
