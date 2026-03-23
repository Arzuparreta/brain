import os
from pathlib import Path

from brain.commands import install_completions
from brain.paths import brain_root

PATH_MARKER = "# brain-cli-path (managed by brain setup)"


def _append_path_block(rc_file: Path, block_lines: list[str], bin_dir: str) -> None:
    rc_file.parent.mkdir(parents=True, exist_ok=True)
    content = rc_file.read_text(encoding="utf-8") if rc_file.exists() else ""
    if PATH_MARKER in content and bin_dir in content:
        print(f"PATH already configured in {rc_file}")
        return

    append = "\n" + PATH_MARKER + "\n" + "\n".join(block_lines) + "\n"
    with rc_file.open("a", encoding="utf-8") as f:
        f.write(append)
    print(f"Added {bin_dir} to PATH in {rc_file} (new shells will have the brain command).")


def _configure_path() -> None:
    root = brain_root()
    bin_dir = str(root / "bin")
    shell_base = Path(os.environ.get("SHELL", "bash")).name

    if shell_base == "fish":
        fish_rc = Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))) / "fish" / "config.fish"
        _append_path_block(
            fish_rc,
            [f'test -d "{bin_dir}"; and fish_add_path "{bin_dir}"'],
            bin_dir,
        )
        return

    if shell_base == "zsh":
        zsh_root = Path(os.environ.get("ZDOTDIR", str(Path.home())))
        zsh_rc = zsh_root / ".zshrc"
        _append_path_block(zsh_rc, [f'export PATH="{bin_dir}:$PATH"'], bin_dir)
        return

    bash_rc = Path.home() / ".bashrc"
    _append_path_block(bash_rc, [f'export PATH="{bin_dir}:$PATH"'], bin_dir)


def setup() -> None:
    """Set up PATH integration and Fish completions."""
    _configure_path()
    try:
        install_completions.install_completions()
    except Exception:
        print("Fish not detected or completions install failed; skipped tab completions.")

    print("")
    print("Open a new terminal (or source your shell rc) then try: brain list")
    print("")
    print("Brain is ready.")
