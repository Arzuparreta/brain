# Brain

Brain is the ultra simple **CLI** that I use to **manage** a plain **list of .md** files  
of any kind. It just adds, removes, edit and list .md files in a directory.

You will not find anything fancy here. This just solves the problem of  
having to get out of your terminal instance to read or note something,  
that's it.

Editor and note extension are configurable in `settings.json` at the repo root  
(next to `pyproject.toml`).

First time, from this directory:

```bash
./scripts/setup.sh
```

Then open a new terminal (or reload your shell config) and use `brain` from anywhere.

## Commands

``brain edit <file_name>``: Open the file with the given name in the  
configured text editor. If the file does not exist, root brain  
directory will be opened in your text editor.

``brain add <file_name>``: Add a new file with the given name. If already  
exists works like edit.

``brain remove <file_name>``: Remove the file with the given name. If the file  
does not exist, nothing will happen.

``brain list``: List all files in the configured directory.

``brain rename <old> <new>``: Rename a file.

``brain see <file_name>``: Print a file to the terminal.
