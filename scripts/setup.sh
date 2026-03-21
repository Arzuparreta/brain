#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/bin"
BRAIN_EXEC="$BIN/brain"
INSTALL_SHELL=1

for arg in "$@"; do
    case "$arg" in
        --no-path|--no-shell) INSTALL_SHELL=0 ;;
        -h|--help)
            echo "Usage: ./scripts/setup.sh [--no-path]"
            echo "  Creates .venv, installs dependencies, configures your shell PATH, and (if Fish is"
            echo "  present) installs tab completions using an absolute path to this repo's bin/brain."
            echo "  --no-path  Skip PATH and completion changes (venv + pip only)."
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

brain_path_marker="# brain-cli-path (managed by brain/scripts/setup.sh)"

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

install_fish_completions() {
    if ! command -v fish >/dev/null 2>&1 && [ ! -d "${XDG_CONFIG_HOME:-$HOME/.config}/fish" ]; then
        echo "Fish not detected; skipped tab completions (install fish and re-run ./scripts/setup.sh)."
        return 0
    fi
    local comp_dir="${XDG_CONFIG_HOME:-$HOME/.config}/fish/completions"
    local comp_file="$comp_dir/brain.fish"
    mkdir -p "$comp_dir"
    local subcmds
    subcmds=$(cd "$ROOT" && .venv/bin/python -c "from brain.constants import FISH_SUBCOMMANDS; print(' '.join(FISH_SUBCOMMANDS))")
    # Single-quoted path for fish: escape embedded single quotes
    local q_exec
    q_exec=$(printf '%s\n' "$BRAIN_EXEC" | sed "s/'/'\\\\''/g")
    cat >"$comp_file" <<EOF
# brain-cli-completions (managed by brain/scripts/setup.sh — do not edit by hand)
function __brain_complete_files
    command '$q_exec' complete_files
end

complete -c brain -f
complete -c brain -n "__fish_use_subcommand" -a "$subcmds"
complete -c brain -n "__fish_seen_subcommand_from edit remove see" -a "(__brain_complete_files)"
complete -c brain -n "__fish_seen_subcommand_from rename" -a "(__brain_complete_files)"
EOF
    echo "Installed Fish tab completions at $comp_file"
}

if [ "$INSTALL_SHELL" -eq 1 ]; then
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
    install_fish_completions
    echo ""
    echo "Open a new terminal (or: source ~/.bashrc | source ~/.zshrc | start a new fish) then try: brain list"
else
    echo "Skipped shell integration (--no-path). Add PATH manually: export PATH=\"$BIN:\$PATH\""
fi

echo ""
echo "Brain is ready."
