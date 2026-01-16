import logging

from pydantic import Field, validate_call

from translation_library.utils.config_utils import (
    get_all_english_names,
    get_all_native_names,
    get_language_file_path,
)
from translation_library.utils.toml_utils import get_value_from_key

logger = logging.getLogger(__name__)


def get_languages(lowercase: bool = False) -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its native spelling:

    >>> ["English", "Deutsch", "Español"]

    Returns:
        list[str]: list of all supported languages with their native spelling
    """
    logger.debug("Attempting to retrieve list of supported languages")
    if lowercase:
        return [name.lower() for name in get_all_native_names()]
    return get_all_native_names()


def get_languages_as_english_names(lowercase: bool = False) -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its english
    spelling:

    >>> ["english", "german", "spanish"]

    Returns:
        list[str]: list of all supported languages with their english spelling
    """
    logger.debug("Attempting to retrieve list of supported languages as english names")
    if lowercase:
        return [name.lower() for name in get_all_english_names()]
    return get_all_english_names()


@validate_call
def is_supported(language: str = Field(..., min_length=1)) -> bool:
    """
    Checks to see if a given language is supported.

    Args:
        language (str): the name of the language to check if support

    Returns:
        bool: `True` if the language is supported, `False` otherwise
    """
    supported: bool = language.lower() in get_languages(
        lowercase=True
    ) or language.lower() in get_languages_as_english_names(lowercase=True)

    logger.debug("'%s' is supported? '%s'", language, str(supported))
    return supported


@validate_call
def get_i18n_obj(
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
