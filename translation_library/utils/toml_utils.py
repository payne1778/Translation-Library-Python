from os.path import exists
from pathlib import Path
from typing import Any

import dpath.util
import tomlkit


def serialize_toml_dict(toml_file_path: str | Path) -> dict:
    # """
    # Return a toml file as a dictionary of key-value pairs from a specified
    # directory path.

    # :param toml_file_path: The path to the toml file to be loaded
    # :return: The entire toml file represented as a dict
    # """
    if not exists(toml_file_path):
        raise ValueError(f"'{toml_file_path}' does not exist")
    with open(toml_file_path, "rb") as f:
        return tomlkit.load(f)


def deserialize_toml_dict(toml_data: dict, toml_file_path: str | Path) -> None:
    if not exists(toml_file_path):
        raise ValueError(f"'{toml_file_path}' does not exist")
    with open(toml_file_path, "w") as f:
        return tomlkit.dump(toml_data, f)


def update_keys(toml_file_path: str | Path, key: str, new_value: Any) -> None:
    if not exists(toml_file_path):
        raise ValueError(f"'{toml_file_path}' does not exist")
    toml_data: dict = serialize_toml_dict(toml_file_path)
    dpath.util.set(toml_data, f"**/{key}", new_value)
    deserialize_toml_dict(toml_data, toml_file_path)


def update_value(toml_file_path: str | Path, key_path: str, new_value: Any) -> None:
    if not exists(toml_file_path):
        raise ValueError(f"'{toml_file_path}' does not exist")
    toml_data: dict = serialize_toml_dict(toml_file_path)
    dpath.util.set(toml_data, key_path, new_value)
    deserialize_toml_dict(toml_data, toml_file_path)
