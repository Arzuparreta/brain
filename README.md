# Brain

Brain is a small **CLI** for managing a plain **list of markdown files**: add, remove, edit, list, rename, and print notes. Everything lives in **one folder** you can clone, move, or copy.

## Portable install (recommended)

All code, your virtualenv, `settings.json`, and `brain_data` stay **inside** the Brain directory. First-time setup configures your shell **PATH** and, when Fish is available, **tab completions** (no separate completion step).

1. Clone or copy this repository to wherever you want (e.g. `~/brain`).

2. From that directory, run **once**:

   ```bash
   ./scripts/setup.sh
   ```

   This:

   - Creates `.venv/` and installs dependencies into it (still inside this folder).
   - Appends a small block to your shell startup file (`~/.bashrc`, `~/.zshrc`, or Fish’s `config.fish`, based on `$SHELL`) so `PATH` includes `<this-repo>/bin`. **Idempotent:** running setup again does not duplicate the PATH block if the path is already there.
   - If **Fish** is installed (or `~/.config/fish` already exists), writes `~/.config/fish/completions/brain.fish` using the **absolute path** to this repo’s `bin/brain`, so completions work even before `PATH` is applied in subshells. Re-running setup **refreshes** that file (e.g. after you move the repo).

   `./scripts/bootstrap.sh` is a deprecated alias for `./scripts/setup.sh`.

3. **Open a new terminal** (or reload your shell config), then from **any** directory:

   ```bash
   brain list
   ```

Use `./scripts/setup.sh --no-path` if you only want the venv and **no** changes to shell config or Fish completions.

If you **move** the Brain folder, remove the old `# brain-cli-path` block from your shell config if needed, delete or ignore the old Fish completion file, then run `./scripts/setup.sh` again from the new location.

### Layout

| Path | Purpose |
|------|---------|
| `bin/brain` | Shell launcher: sets `BRAIN_ROOT`, runs `.venv/bin/python -m brain` |
| `.venv/` | Python + dependencies (only used by this project) |
| `brain/` | Application package |
| `brain_data/` | Your notes (default; ignored by git by default) |
| `settings.json` | Optional overrides (editor, extension, `FILES_DIR`, …) at **repo root** |

`settings.json` is always read from **`BRAIN_ROOT/settings.json`**, not from your shell’s current working directory.

### Running without `bin/brain`

After setup, you can also run:

```bash
.venv/bin/python -m brain list
```

`BRAIN_ROOT` is inferred from the package location when unset.

### Fish completions

Normally you do **nothing** beyond `./scripts/setup.sh`. To refresh completions after moving the repo, run setup again.

The repo file `brain.fish` is optional reference material; the installed file lives under `~/.config/fish/completions/`. You can also run `brain install_completions` to rewrite that file from Python (same result as setup).

## Configuration

Edit `settings.json` at the **root of this repository** (next to `pyproject.toml`). Keys match the uppercase names in `brain/config.py` (e.g. `TEXT_EDITOR`, `NOTE_EXTENSION`, `FILES_DIR`). Environment variables still override those keys when set.

## Commands

- `brain edit [name]` — Open a note in your editor, or open `brain_data` if the name is missing or unknown.
- `brain add <name>` — Create/open a note.
- `brain remove <name>` — Delete a note.
- `brain list` — List files in `brain_data`.
- `brain rename <old> <new>` — Rename a note.
- `brain see <name>` — Print a note to the terminal.
