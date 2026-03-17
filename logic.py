from settings import settings
import click
from config import FILES_DIR


editor = settings["TEXT_EDITOR"]
extension = settings["NOTE_EXTENSION"]
dir = settings["FILES_DIR"]


def get_brain_data_dir():
    """Return the brain data and create it if it doesn't exist."""
    FILES_DIR.mkdir(exist_ok=True)
    return FILES_DIR


@click.group()
def cli():
    pass
