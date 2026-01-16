import logging

import tomlkit
from pydantic import Field, validate_call

from translation_library.utils.config_utils import get_language_file_path
from translation_library.utils.toml_utils import serialize_toml_dict
from translation_library.utils.translation_utils import is_supported

logger = logging.getLogger(__name__)


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
    logger.debug("Printing '%s.toml'", language)
    print(into_toml_str(language))
