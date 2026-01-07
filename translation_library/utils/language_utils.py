from typing import Annotated

import tomlkit
from pydantic import Field, validate_call

from translation_library.utils.path_utils import (
    get_language_file_path,
    get_languages_file_path,
)
from translation_library.utils.toml_utils import serialize_toml_dict


@validate_call
def language_toml_dict(language: Annotated[str, Field(min_length=1)]) -> dict:
    """
    Returns a TOML-like dictionary of a specified language

    Args:
        language (str): the language to convert into a TOML-like dict

    Returns:
        dict: the language file as a TOML-like dict
    """
    return serialize_toml_dict(get_language_file_path(language))


def languages_toml_dict() -> dict:
    """
    Returns a TOML-like dictionary of all of the translation library's supported
    languages

    Returns:
        dict: TOML-like dict of supported languages
    """
    return serialize_toml_dict(get_languages_file_path())


def get_languages() -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its local spelling.

    :return: A list of all of the supported languages with local spelling
    """
    return [language for language in languages_toml_dict().values()]


def get_languages_anglicized() -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its anglicized
    spelling.

    :return: A list of all of the supported languages with anglicized spelling
    """
    return [language for language in languages_toml_dict()]


@validate_call
def is_supported_language(language: Annotated[str, Field(min_length=1)]) -> bool:
    """
    Checks to see if a given language is supported.

    :param language: the name of the language to be checked
    :return: `True` if the language is supported, `False` otherwise
    """
    return get_languages_anglicized().__contains__(
        language.lower()
    ) or get_languages().__contains__(language.lower())


@validate_call
def into_language_toml_str(language: Annotated[str, Field(min_length=1)]) -> str:
    return tomlkit.dumps(language_toml_dict(language))


@validate_call
def print_language_toml_dict(language: Annotated[str, Field(min_length=1)]) -> None:
    print(into_language_toml_str(language))


# def get_values_from_key(language: str, key: str) -> None:
#     print(dpath.get(language_toml(language), f"**/{key}"))
