#################################################
# Do not configure anything in this file;       #
# use settings.json at the Brain repo root.     #
#################################################

from pathlib import Path

from brain.paths import brain_root

# directory for brain data (under Brain repo root)
FILES_DIR = brain_root() / "brain_data"

# default note extension
NOTE_EXTENSION = "md"

# default text editor for editing notes
TEXT_EDITOR = "nvim"
