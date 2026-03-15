from pathlib import Path

# directory for brain data (You can change this directly!!)
FILES_DIR = Path(__file__).parent.resolve() / "brain_data"

# default text editor for editing notes
TEXT_EDITOR = "nvim"  # Change this to your preferred text editor


def get_brain_data_dir():
    """Return the brain data and create it if it doesn't exist."""
    FILES_DIR.mkdir(exist_ok=True)
    return FILES_DIR
