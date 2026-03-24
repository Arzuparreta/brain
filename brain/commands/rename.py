from brain.logic import note_path


def rename_files(old_name, new_name):
    """Rename something from your brain."""
    old_path = note_path(old_name)
    new_path = note_path(new_name)
    ext = new_path.suffix
    try:
        old_path.rename(new_path)
    except FileNotFoundError:
        print("Failed to rename file.")
        return
    except OSError:
        print("Failed to rename file.")
        return
    print(f"File renamed to {new_name}{ext}")
