import argparse
import sys

from brain import __version__, logic
from brain.commands import (
    add,
    completions,
    edit,
    install_completions,
    list,
    remove,
    rename,
    see,
    setup,
    think,
)


def main():
    # Internal subcommand used by fish completions — handle before argparse
    # so it never appears in user-facing help.
    if len(sys.argv) > 1 and sys.argv[1] == "complete_files":
        logic.ensure_notes_dir()
        completions.complete_files()
        return
    # Keep completion installation available, but hidden from normal help.
    if len(sys.argv) > 1 and sys.argv[1] == "install_completions":
        if any(arg in ("-h", "--help") for arg in sys.argv[2:]):
            print("usage: brain install_completions")
            print("")
            print("Write Fish completions to ~/.config/fish/completions/brain.fish")
            return
        logic.ensure_notes_dir()
        install_completions.install_completions()
        return

    parser = argparse.ArgumentParser(
        prog="brain",
        description="| Your brain in your terminal. |",
    )
    parser.add_argument("--version", action="version", version=f"brain {__version__}")

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("add", help="stick something to your brain.").add_argument("name")

    p_edit = sub.add_parser("edit", help="edit the brain data files.")
    p_edit.add_argument("name", nargs="?", default=None)

    sub.add_parser("list", help="list your brain files.")

    sub.add_parser("remove", help="delete something from your brain.").add_argument(
        "name"
    )

    p_rename = sub.add_parser("rename", help="rename something from your brain.")
    p_rename.add_argument("old_name")
    p_rename.add_argument("new_name")

    sub.add_parser("see", help="print file content to the terminal.").add_argument(
        "name"
    )

    sub.add_parser("think", help="list links between notes.")
    sub.add_parser("setup", help="set up completions and global brain command support.")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    logic.ensure_notes_dir()

    match args.command:
        case "add":
            add.add_files(args.name)
        case "edit":
            edit.edit_files(args.name)
        case "list":
            list.list_files()
        case "remove":
            remove.remove_files(args.name)
        case "rename":
            rename.rename_files(args.old_name, args.new_name)
        case "see":
            see.see_files(args.name)
        case "think":
            think.think()
        case "setup":
            setup.setup()
