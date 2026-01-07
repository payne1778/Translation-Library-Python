import tomlkit
from pydantic import Field, validate_call

from translation_library.utils.path_utils import (
    get_language_file_path,
    get_languages_file_path,
)
from translation_library.utils.toml_utils import get_value_from_key, serialize_toml_dict


@validate_call
def language_toml_dict(language: str = Field(..., min_length=1)) -> dict:
    """
    Returns a TOML-like dictionary of a specified language.

    Args:
        language (str): the language to convert into a TOML-like dict

    Returns:
        dict: the language file as a TOML-like dict
    """
    return serialize_toml_dict(get_language_file_path(language))


def languages_toml_dict() -> dict:
    """
    Returns a TOML-like dictionary of all of the translation library's supported
    languages. Example:

    >>> {"english": "English, "german": "Deutsch"}

    Returns:
        dict: TOML-like dict of supported languages
    """
    return serialize_toml_dict(get_languages_file_path())


def get_languages() -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its native spelling:

    >>> ["English", "Deutsch"]

    Returns:
        list[str]: list of all supported languages with their native spelling
    """
    return [language for language in languages_toml_dict().values()]


def get_languages_anglicized() -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its anglicized
    spelling:

    >>> ["english", "german"]

    Returns:
        list[str]: list of all supported languages with their anglicized spelling
    """
    return [language for language in languages_toml_dict()]


@validate_call
def is_supported_language(language: str = Field(..., min_length=1)) -> bool:
    """
    Checks to see if a given language is supported.

    Args:
        language (str): the name of the language to check if support

    Returns:
        bool: `True` if the language is supported, `False` otherwise
    """
    return get_languages_anglicized().__contains__(
        language.lower()
    ) or get_languages().__contains__(language.lower())


@validate_call
def into_language_toml_str(language: str = Field(..., min_length=1)) -> str:
    """
    Return the TOML language file of a specified language as a str.

    Args:
        language (str): the name of the language TOML dict to convert into a str
    """
    return tomlkit.dumps(language_toml_dict(language))


@validate_call
def print_language_toml_dict(language: str = Field(..., min_length=1)) -> None:
    """
    Pretty print, or print with TOML-based formatting, the language file of a
    specified language.

    Args:
        language (str): the name of the language TOML dict to pretty print
    """
    print(into_language_toml_str(language))


@validate_call
def get_value_from_language_toml(
    language: str = Field(..., min_length=1), key_path: str = Field(..., min_length=1)
) -> object:
    """
    Get the value of a specific key from a given language TOML file.

    Args:
        language (str): the name of the language TOML dict to get value from
        key_path (str): the path to the key in the specified language TOML dict

    Returns:
        object: the value of a given key
    """
    return get_value_from_key(get_language_file_path(language), key_path)
