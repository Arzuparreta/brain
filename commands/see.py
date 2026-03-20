import click

from logic import dir, extension


@click.command(name="see")
@click.argument("name")
def see_files(name):
    try:
        with open(dir / f"{name}.{extension}", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permission to read this file")
