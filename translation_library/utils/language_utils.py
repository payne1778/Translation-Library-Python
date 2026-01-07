import logging
from pathlib import Path

import tomlkit
from pydantic import Field, validate_call

from translation_library.utils.path_utils import (
    get_language_file_path,
    get_languages_file_path,
    get_project_root,
)
from translation_library.utils.toml_utils import get_value_from_key, serialize_toml_dict

logger = logging.getLogger(__name__)


def local_get_language_file_path(code: str) -> Path:
    config_path: Path = Path(get_project_root() / "config.toml")
    i18n_dir: Path = Path(str(get_value_from_key(config_path, "paths.i18n_dir")))
    language_file_path: Path = Path(
        str(get_value_from_key(config_path, f"languages.{code.lower()}.file"))
    )
    return get_project_root() / i18n_dir / language_file_path


@validate_call
def into_toml_dict(language: str = Field(..., min_length=1)) -> dict:
    """
    Returns a TOML-like dictionary of a specified language.

    Args:
        language (str): the language to convert into a TOML-like dict

    Returns:
        dict: the language file as a TOML-like dict or {} if file was empty
    """
    logger.debug("Attempting to retrieve TOML dict from '%s.toml'", language)
    if toml_dict := serialize_toml_dict(get_language_file_path(language)):
        logger.info("Successfuly retrieved toml dict from '%s.toml'", language)
        return toml_dict
    logger.warning("None dict retrieved from '%s.toml'", language)
    return {}


def get_languages_toml_dict() -> dict:
    """
    Returns a TOML-like dictionary of all of the translation library's supported
    languages. Example:

    >>> {"english": "English, "german": "Deutsch", "spanish": "Español"}

    Returns:
        dict: TOML-like dict of supported languages or {} if file was empty
    """
    logger.debug("Attempting to retrieve TOML dict from 'languages.toml'")
    if toml_dict := serialize_toml_dict(get_languages_file_path()):
        logger.info("Successfuly retrieved toml dict from 'languages.toml'")
        return toml_dict
    logger.warning("None dict retrieved from 'languages.toml'")
    return {}


@validate_call
def into_toml_str(language: str = Field(..., min_length=1)) -> str:
    """
    Return the TOML language file of a specified language as a TOML-based
    pretty str.

    Args:
        language (str): the name of the language TOML dict to convert into a str
    """
    if not is_supported(language):
        logger.error("is_supported() returned False for language arg '%s'", language)
        raise ValueError(f"{language} is not supported")

    logger.debug("Converting '%s.toml' as a dictionary into str")
    if toml_str := tomlkit.dumps(into_toml_dict(language)):
        logger.info("Successfully converted the '%s' TOML dict into str")
        return toml_str
    logger.warning("None received from into_toml_dict() with arg '%s'", language)
    return ""


@validate_call
def print_toml_dict(language: str = Field(..., min_length=1)) -> None:
    """
    Pretty print, or print with TOML-based formatting, the language file of a
    specified language.

    Args:
        language (str): the name of the language TOML dict to pretty print
    """
    print(into_toml_str(language))


def get_languages() -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its native spelling:

    >>> ["English", "Deutsch", "Español"]

    Returns:
        list[str]: list of all supported languages with their native spelling
    """
    logger.debug("Attempting to retrieve list of supported languages")
    return [language for language in get_languages_toml_dict().values()]


def get_languages_anglicized() -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its anglicized
    spelling:

    >>> ["english", "german", "spanish"]

    Returns:
        list[str]: list of all supported languages with their anglicized spelling
    """
    logger.debug("Attempting to retrieve list of supported languages anglicized")
    return [language for language in get_languages_toml_dict()]


@validate_call
def is_supported(language: str = Field(..., min_length=1)) -> bool:
    """
    Checks to see if a given language is supported.

    Args:
        language (str): the name of the language to check if support

    Returns:
        bool: `True` if the language is supported, `False` otherwise
    """
    supported: bool = language.lower() in [
        l.lower() for l in get_languages_anglicized()
    ] or language.lower() in [l.lower() for l in get_languages()]

    logger.debug("'%s' is supported? '%s'", language, str(supported))
    return supported


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
    logger.debug("Getting '%s' from the '%s' TOML file" % (key_path, language))
    if value := get_value_from_key(get_language_file_path(language), key_path):
        logger.info(
            "Successfuly retrieved '%s' with key '%s' from '%s.toml'",
            value,
            key_path,
            language,
        )
        return value
    logger.warning(
        "None value retrieved with key '%s' from '%s.toml'", key_path, language
    )
    return None
