from pathlib import Path
from typing import Annotated

import tomlkit
from glom import glom  # type: ignore
from pydantic import BeforeValidator, Field, validate_call

from translation_library.utils.path_utils import (
    get_language_file_path,
    valid_path_validator,
)


@validate_call
def serialize_toml_dict(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_path_validator)],
) -> dict:
    """
    Return a TOML file as a dictionary of key-value pairs from a specified
    directory path.

    Args:
        toml_file_path (str | Path): path of the TOML file to be loaded

    Returns:
        dict: entire TOML file as a dict
    """
    with open(toml_file_path, "rb") as f:
        return tomlkit.load(f)


@validate_call
def deserialize_toml_dict(
    toml_data: Annotated[dict, Field(min_length=1)],
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_path_validator)],
) -> None:
    """
    Write a TOML-like dictionary to a specified directory path.

    Args:
        toml_data (dict): TOML-like dictionary to be deserialized
        toml_file_path (str | Path): path of the TOML file to write to
    """
    with open(toml_file_path, "w") as f:
        return tomlkit.dump(toml_data, f)


@validate_call
def get_value_from_key(
    language: Annotated[str, Field(min_length=1)],
    key_path: Annotated[str, Field(min_length=1)],
) -> object:
    try:
        language_toml_dict: dict = serialize_toml_dict(get_language_file_path(language))
        return glom(language_toml_dict, key_path)
    except Exception as e:
        raise RuntimeError(f"An exception occured: {e}") from e
