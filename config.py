#################################################
# Do not configure anything in this file;       #
# instead, go to /settings.json in the root dir.#
#################################################

from pathlib import Path

# directory for brain data
FILES_DIR = Path(__file__).parent.resolve() / "brain_data"

# default note extension
NOTE_EXTENSION = "md"

# default text editor for editing notes
TEXT_EDITOR = "nvim"
