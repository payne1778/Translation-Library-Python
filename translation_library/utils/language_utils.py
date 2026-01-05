from translation_library.utils.path_utils import get_languages_file_path
from translation_library.utils.toml_utils import serialize_toml


def language_toml(language: str) -> dict:
    """
    _Returns a toml dictionary of a specified language_

    Args:
        language (str): _the language to convert into toml_

    Returns:
        dict: _the language file as a toml dictonary_
    """
    return serialize_toml(get_languages_file_path())


def languages_toml() -> dict:
    """
    _Returns a toml dictionary of all of the translation library's supported
    languages_

    Returns:
        dict: _toml dict of supported languages_
    """
    return serialize_toml(get_languages_file_path())


def get_languages() -> list[str]:
    """
    Returns a list of all supported languages according to the languages toml
    file. Each entry in the list is the language spelled in its local spelling.

    :return: A list of all of the supported languages with local spelling
    """
    return [language for language in languages_toml().values()]


def get_languages_anglicized() -> list[str]:
    """
    Returns a list of all supported languages according to the languages toml
    file. Each entry in the list is the language spelled in its anglicized
    spelling.

    :return: A list of all of the supported languages with anglicized spelling
    """
    return [language for language in languages_toml()]


def is_supported_language(language: str) -> bool:
    """
    Checks to see if a given language is supported.

    :param language: the name of the language to be checked
    :return: `True` if the language is supported, `False` otherwise
    """
    return get_languages_anglicized().__contains__(
        language.lower()
    ) or get_languages().__contains__(language.lower())
