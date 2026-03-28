# Brain

Brain is the ultra simple **CLI** that I use to **manage** a plain **list of .md** files  
of any kind. It just adds, removes, edits and lists .md files in a directory.

You will not find anything fancy here. This just solves the problem of  
having to get out of your terminal instance to read or note something,  
that's it.

Python 3.10 or newer. No external dependencies. No pip install. No venv.

Run `bin/brain` using a full path from wherever you are (`…/brain/bin/brain list`), or `./bin/brain` when your shell is already in the repo.

If you want to type `brain` instead of the path, run `./bin/brain setup` once. It adds this repo's `bin` to your PATH for Fish, zsh, or bash, and on Fish it installs tab completions. `scripts/setup.sh` does the same thing. Then open a new terminal or source your shell config.

For `add`, `edit`, `see`, `remove`, and `rename`, pass the note **name** only — not `something.md`. The extension comes from `settings.json` (default `md`). `edit` with no name opens the notes folder in your editor. `think` shows links between notes if you use wiki-style links. The rest is in `brain --help`.

Notes sit in `brain_data/`. `settings.json` next to `pyproject.toml` is for the editor command and note extension if you do not want the defaults.

If the repo lives on a shared drive, the markdown goes with it. Each machine still needs Python; PATH and completions from `setup` are per machine.
