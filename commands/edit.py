import click

import subprocess

from logic import editor, dir


@click.command(name="edit")
@click.argument("name", required=False)
def edit_files(name):
    """Edit the brain data files."""
    file_path = dir
    if name:
        file_path = dir / f"{name}.md"
    if file_path.exists():
        try:
            subprocess.run(editor.split() + [str(file_path)], check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Error opening editor: {e}")
    else:
        file_path = dir
        try:
            subprocess.run(editor.split() + [str(file_path)])
        except subprocess.CalledProcessError as e:
            click.echo(f"Error opening editor: {e}")
