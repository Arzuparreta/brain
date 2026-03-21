# Brain

Brain is a small **CLI** for managing a plain **list of markdown files**: add, remove, edit, list, rename, and print notes. Everything lives in **one folder** you can clone, move, or copy.

## Portable install (recommended)

All code, your virtualenv, `settings.json`, and `brain_data` stay **inside** the Brain directory. Setup adds your repo’s `bin/` directory to your shell config once so the `brain` command is found from anywhere.

1. Clone or copy this repository to wherever you want (e.g. `~/brain`).

2. From that directory, run **once**:

   ```bash
   ./scripts/bootstrap.sh
   ```

   This:

   - Creates `.venv/` and installs dependencies into it (still inside this folder).
   - Appends a small block to your shell startup file (`~/.bashrc`, `~/.zshrc`, or Fish’s `config.fish`, based on `$SHELL`) so `PATH` includes `<this-repo>/bin`. It is **idempotent**: running bootstrap again does not duplicate the block if the path is already there.

3. **Open a new terminal** (or `source` your rc file), then from **any** directory:

   ```bash
   brain list
   ```

Use `./scripts/bootstrap.sh --no-path` if you only want the venv and **no** changes to shell config (you would manage `PATH` yourself).

If you **move** the Brain folder to a new path, remove the old `# brain-cli-path` block from your shell config (or run bootstrap from the new location after cleaning the old lines), then run `./scripts/bootstrap.sh` again so `PATH` points at the new `bin/`.

### Layout

| Path | Purpose |
|------|---------|
| `bin/brain` | Shell launcher: sets `BRAIN_ROOT`, runs `.venv/bin/python -m brain` |
| `.venv/` | Python + dependencies (only used by this project) |
| `brain/` | Application package |
| `brain_data/` | Your notes (default; ignored by git by default) |
| `settings.json` | Optional overrides (editor, extension, `FILES_DIR`, …) at **repo root** |

`settings.json` is always read from **`BRAIN_ROOT/settings.json`**, not from your shell’s current directory, so behavior stays consistent when you run `brain` from anywhere.

### Running without `bin/brain`

After bootstrap, you can also run:

```bash
.venv/bin/python -m brain list
```

`BRAIN_ROOT` is inferred from the package location (parent of the `brain` package) when unset.

### Fish completions (portable)

The file `brain.fish` in this repo is portable. Source it from your config, for example:

```fish
source /path/to/brain/brain.fish
```

The command `brain install_completions` writes under `~/.config/fish/` (not inside the Brain folder); use it only if you accept that.

## Configuration

Edit `settings.json` at the **root of this repository** (next to `pyproject.toml`). Keys match the uppercase names in `brain/config.py` (e.g. `TEXT_EDITOR`, `NOTE_EXTENSION`, `FILES_DIR`). Environment variables still override those keys when set.

## Commands

- `brain edit [name]` — Open a note in your editor, or open `brain_data` if the name is missing or unknown.
- `brain add <name>` — Create/open a note.
- `brain remove <name>` — Delete a note.
- `brain list` — List files in `brain_data`.
- `brain rename <old> <new>` — Rename a note.
- `brain see <name>` — Print a note to the terminal.
