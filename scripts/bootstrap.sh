#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/bin"
INSTALL_PATH=1

for arg in "$@"; do
    case "$arg" in
        --no-path) INSTALL_PATH=0 ;;
        -h|--help)
            echo "Usage: ./scripts/bootstrap.sh [--no-path]"
            echo "  Sets up .venv, installs dependencies, and adds $BIN to your shell PATH (once)."
            echo "  --no-path  Skip modifying shell config (only create venv + pip install)."
            exit 0
            ;;
    esac
done

cd "$ROOT"
if [ ! -d .venv ]; then
    python3 -m venv .venv
fi
.venv/bin/pip install -q --upgrade pip
.venv/bin/pip install -q -e .

brain_path_marker="# brain-cli-path (managed by brain/scripts/bootstrap.sh)"

append_path_bash_zsh() {
    local rc_file=$1
    mkdir -p "$(dirname "$rc_file")"
    if [ -f "$rc_file" ] && grep -qF "$brain_path_marker" "$rc_file" && grep -qF "$BIN" "$rc_file"; then
        echo "PATH already configured in $rc_file"
        return 0
    fi
    {
        echo ""
        echo "$brain_path_marker"
        echo "export PATH=\"$BIN:\$PATH\""
    } >>"$rc_file"
    echo "Added $BIN to PATH in $rc_file (new shells will have the brain command)."
}

append_path_fish() {
    local rc_file="${XDG_CONFIG_HOME:-$HOME/.config}/fish/config.fish"
    mkdir -p "$(dirname "$rc_file")"
    if [ -f "$rc_file" ] && grep -qF "$brain_path_marker" "$rc_file" && grep -qF "$BIN" "$rc_file"; then
        echo "PATH already configured in $rc_file"
        return 0
    fi
    {
        echo ""
        echo "$brain_path_marker"
        echo "test -d \"$BIN\"; and fish_add_path \"$BIN\""
    } >>"$rc_file"
    echo "Added $BIN to PATH in $rc_file (new shells will have the brain command)."
}

if [ "$INSTALL_PATH" -eq 1 ]; then
    shell_base=$(basename "${SHELL:-bash}")
    case "$shell_base" in
        fish)
            append_path_fish
            ;;
        zsh)
            append_path_bash_zsh "${ZDOTDIR:-$HOME}/.zshrc"
            ;;
        *)
            append_path_bash_zsh "$HOME/.bashrc"
            ;;
    esac
    echo ""
    echo "Open a new terminal (or run: source ~/.bashrc  /  source ~/.zshrc) then try: brain list"
else
    echo "Skipped PATH install (--no-path). Add manually: export PATH=\"$BIN:\$PATH\""
fi

echo ""
echo "Brain is ready."
