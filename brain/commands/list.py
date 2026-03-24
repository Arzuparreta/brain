from brain.logic import notes_dir


def list_files():
    """List your brain files."""
    files = [f.name for f in notes_dir().iterdir() if f.is_file()]
    if not files:
        print("Your brain is empty.")
    else:
        print("Your brain:")
        for file in files:
            print(f"- {file}")
