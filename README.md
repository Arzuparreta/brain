# Brain

Brain is an ultra simple CLI that I use to manage a plain **list of .md** files  
of any kind. It just adds, removes, edit and list .md files in a directory.

You will not find anything fancy here. This just solves my problem of having to get out of a terminal instance to read or note something, and lets me have "dockerized" notes using an existant samba share, for example.

## Requirements

- Python 3.10+

No external dependencies. No pip install. No venv.

## Usage

Run directly from the repo:

```bash
./bin/brain list
```

Or with an absolute path from anywhere:

```bash
/path/to/brain/bin/brain list
```

### Set up `brain`

Run setup once to configure completions and support using `brain` as a bare command from any directory:

```bash
./bin/brain setup
```

Then open a new terminal (or reload your shell config) and use `brain` from anywhere.

Editor and note extension are configurable in `settings.json` at the repo root  
(next to `pyproject.toml`).

## Commands

``brain add <file_name>``: Add a new file with the given name. If already  
exists works like edit.

``brain edit <file_name>``: Open the file with the given name in the  
configured text editor. If the file does not exist, root brain  
directory will be opened in your text editor.

``brain list``: List all files in the configured directory.

``brain remove <file_name>``: Remove the file with the given name. If the file  
does not exist, nothing will happen.

``brain rename <old> <new>``: Rename a file.

``brain see <file_name>``: Print a file to the terminal.

``brain think``: List links between notes (wikilinks + word multiset).

``brain setup``: Set up shell PATH integration and Fish tab completions.

## Shared / multi-machine use

The `brain` directory can live on a shared drive (e.g. Samba). Each machine  
only needs `python3` installed. Notes in `brain_data/` are shared; no  
machine-specific runtime files are written to the repo.
