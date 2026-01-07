from pathlib import Path
from typing import Annotated

import tomlkit
from glom import glom  # type: ignore
from glom.core import PathAccessError  # type: ignore
from pydantic import BeforeValidator, Field, validate_call
from tomlkit.exceptions import EmptyKeyError, EmptyTableNameError

from translation_library.utils.path_utils import valid_path_validator


def valid_toml_path_validator(v: str | Path) -> Path:
    """
    Checks to see if a given path has the `.toml` extension. If so, it will
    call the valid_path_validator from the path_utils module to see if it exists.

    Args:
        v (str | Path): a supposed `str`/`Path` path to a TOML file

    Raises:
        ValueError: if a `str` was given and it does not end in ".toml"
        ValueError: if a `Path` was given and it does not end in ".toml"

    Returns:
        Path: the original path if it exists, otherwise, valid_path_validator() will raise errors
    """
    if isinstance(v, str) and not v.endswith(".toml"):
        # TODO: log this
        raise ValueError("TOML file path must end in .toml")

    if isinstance(v, Path) and v.suffix != ".toml":
        # TODO: log this
        raise ValueError("TOML file path must end in .toml")

    return valid_path_validator(v)


@validate_call
def serialize_toml_dict(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_toml_path_validator)],
) -> dict:
    """
    Return a TOML file as a dictionary of key-value pairs from a specified
    directory path.

    Args:
        toml_file_path (str | Path): the path of the TOML file to be loaded

    Raises:
        RuntimeError: if an unknown/unchecked exception occurs when opening file

    Returns:
        dict: the TOML-like dict obtained from the given TOML language file pah
    """
    try:
        with open(toml_file_path, "rb") as f:
            return tomlkit.load(f)
    except (EmptyKeyError, EmptyTableNameError) as e:
        # TODO: log this
        # if TOML file has invalid syntax
        raise
    except Exception as e:
        # TODO: log this
        raise RuntimeError(f"Could not serialize '{toml_file_path}' due to: {e}")


@validate_call
def deserialize_toml_dict(
    toml_data: Annotated[dict, Field(..., min_length=1)],
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_toml_path_validator)],
) -> None:
    """
    Write a TOML-like dictionary to an specified, pre-existing TOML file path.

    Args:
        toml_file_path (str | Path): TOML-like dictionary to be deserialized
        toml_data (dict): path of the TOML file to write to

    Raises:
        RuntimeError: if an unknown/unchecked exception occurs when writing to file
    """
    try:
        with open(toml_file_path, "w") as f:
            return tomlkit.dump(toml_data, f)
    except (EmptyKeyError, EmptyTableNameError) as e:
        # TODO: log this
        # if TOML file has invalid syntax
        raise
    except Exception as e:
        # TODO: log this
        raise RuntimeError(
            f"Could not deserialize to '{toml_file_path}' due to: {e}"
        ) from e


@validate_call
def get_value_from_key(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_toml_path_validator)],
    key_path: str = Field(..., min_length=1),
) -> object:
    """
    Get the value of a specific key from a given TOML file path.

    Args:
        toml_file_path (str | Path): the path to the TOML dict to get value from
        key_path (str): the path to the key in the specified language TOML dict

    Raises:
        PathAccessError: if the value could not be retrieved from the given key path
        FileNotFoundError: if the arg path to the TOML file does not exist
        RuntimeError: if an unknown/unchecked exception occurs when getting the value

    Returns:
        object: the value associated with the given key path
    """
    try:
        language_toml_dict: dict = serialize_toml_dict(toml_file_path)
        return glom(language_toml_dict, key_path)
    except PathAccessError as pae:
        # TODO: log this
        # if the key does not exist
        raise
    except Exception as ex:
        # TODO: log this
        raise RuntimeError(f"Could not get value from '{toml_file_path}': {ex}") from ex
