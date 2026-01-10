from typing import Annotated, List

import typer  # ignore-errors

app = typer.Typer(no_args_is_help=True, suggest_commands=True)


@app.command()
def list(
    language: Annotated[str, typer.Option("--language", "-l")],
    as_english: Annotated[bool, typer.Option("--english", "-e")] = False,
):
    """
    List supported languages in their native or english spelling.

    Args:
        language (Annotated[str, typer.Option): must have
        as_english (Annotated[bool, typer.Option): not required
    """
    print(f"list {language}")
    print(f"list {as_english}")


# why does this not work?
@app.command()
def translate(
    language: Annotated[str, typer.Option("--language", "-l")],
    key_path: Annotated[str, typer.Option("--key-path", "-k")],
    args: Annotated[List[str], typer.Argument()] = [],
):
    """
    Translate any value from a language TOML file with a specified key.

    Args:
        language (Annotated[str, typer.Option): _description_
        key_path (Annotated[str, typer.Option): _description_
        args (Annotated[dict, typer.Option): _description_
    """
    print(f"translate {language}")
    print(f"translate {key_path}")
    for arg in args:
        print(f"Processing file: {arg}")


@app.command()
def supported(
    language: Annotated[str, typer.Option("--language", "-l")],
):
    """
    Check if a given language is supported by your translation library.

    Args:
        language (Annotated[str, typer.Option): _description_
    """
    print(f"supported {language}")


@app.command()
def get_value(
    language: Annotated[str, typer.Option("--language", "-l")],
    key_path: Annotated[str, typer.Option("--key-path", "-k")],
):
    """
    Get any value from a language TOML file with a specified key.

    Args:
        language (Annotated[str, typer.Option): _description_
        key_path (Annotated[str, typer.Option): _description_
    """
    print(f"get_value {language}")
    print(f"get_value {key_path}")


if __name__ == "__main__":
    app()
