from typing import Annotated, List

import typer  # ignore-errors

from translation_library.utils.translation_utils import (
    get_i18n_obj,
    get_languages,
    get_languages_as_english_names,
    is_supported,
)

cli = typer.Typer(no_args_is_help=True, suggest_commands=True)


@cli.command()
def list(
    language: Annotated[str, typer.Option("--language", "-l")],
    as_english: Annotated[bool, typer.Option("--english", "-e")] = False,
    to_lowercase: Annotated[bool, typer.Option("--to-lowercase", "-t")] = False,
):
    """
    List supported languages in their native or english spelling.

    Args:
        language (str): must have
        as_english (Optional[bool]): not required
    """
    if as_english:
        print(get_languages_as_english_names(lowercase=to_lowercase))
    print(get_languages(lowercase=to_lowercase))


@cli.command()
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
    before_translation: str = str(get_i18n_obj(language.lower(), key_path))
    for arg in args:
        print(f"Processing file: {arg}")


@cli.command()
def supported(
    language: Annotated[str, typer.Option("--language", "-l")],
):
    """
    Check if a given language is supported by your translation library.

    Args:
        language (Annotated[str, typer.Option): _description_
    """
    print(is_supported(language.lower()))


@cli.command()
def i18n_print(
    language: Annotated[str, typer.Option("--language", "-l")],
    key_path: Annotated[str, typer.Option("--key-path", "-k")],
):
    """
    Get any value from a language TOML file with a specified key.

    Args:
        language (Annotated[str, typer.Option): _description_
        key_path (Annotated[str, typer.Option): _description_
    """
    print(get_i18n_obj(language.lower(), key_path))
