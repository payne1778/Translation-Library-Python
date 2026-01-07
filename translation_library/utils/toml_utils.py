from pathlib import Path
from typing import Annotated

import tomlkit
from glom import glom  # type: ignore

# from glom.core import NonExistentKey  # type: ignore
from pydantic import BeforeValidator, Field, validate_call

from translation_library.utils.path_utils import valid_path_validator


# TODO: validate that toml_file_path ends with .toml
@validate_call
def serialize_toml_dict(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_path_validator)],
) -> dict:
    # TODO: fix docstring comment
    """
    Return a TOML file as a dictionary of key-value pairs from a specified
    directory path.

    Args:
        toml_file_path (str | Path): path of the TOML file to be loaded

    Returns:
        dict: entire TOML file as a dict
    """
    try:
        with open(toml_file_path, "rb") as f:
            return tomlkit.load(f)
    except Exception:
        # TODO: log this
        raise


# TODO: validate that toml_file_path ends with .toml
@validate_call
def deserialize_toml_dict(
    toml_data: Annotated[dict, Field(min_length=1)],
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_path_validator)],
) -> None:
    # TODO: fix docstring comment
    """
    Write a TOML-like dictionary to a specified directory path.

    Args:
        toml_data (dict): TOML-like dictionary to be deserialized
        toml_file_path (str | Path): path of the TOML file to write to
    """
    try:
        with open(toml_file_path, "w") as f:
            return tomlkit.dump(toml_data, f)
    except Exception:
        # TODO: log this
        raise


@validate_call
def get_value_from_key(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_path_validator)],
    key_path: Annotated[str, Field(min_length=1)],
) -> object:
    # TODO: docstring comment
    try:
        language_toml_dict: dict = serialize_toml_dict(toml_file_path)
        return glom(language_toml_dict, key_path)
    # TODO: find where this exception is
    # except NonExistentKey as neke:
    #     raise
    except FileNotFoundError as fnfe:
        # TODO: log this
        raise
    except Exception as e:
        # TODO: log this
        raise RuntimeError(f"An exception occurred: {e}") from e
