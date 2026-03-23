from brain.logic import note_path


def see_files(name):
    """Print your files content to the terminal."""
    path = note_path(name)
    try:
        print(path.read_text())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permission to read this file")
