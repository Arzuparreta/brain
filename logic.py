from config import FILES_DIR


def get_brain_data_dir():
    """Return the brain data and create it if it doesn't exist."""
    FILES_DIR.mkdir(exist_ok=True)
    return FILES_DIR
