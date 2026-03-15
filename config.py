from pathlib import Path

# directory for brain data (You can change this directly!!)
NOTES_DIR = Path(__file__).parent.resolve() / "brain_data"

# default text editor for editing notes
USER_EDITOR = "nvim"  # Change this to your preferred text editor


def get_brain_data_dir():
    """Return the notes folder and create it if it doesn't exist."""
    NOTES_DIR.mkdir(exist_ok=True)
    return NOTES_DIR
