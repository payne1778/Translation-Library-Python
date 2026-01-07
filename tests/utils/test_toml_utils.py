import pytest

from tests.utils.constants.values import (
    EXAMPLE_ENGLISH_TOML_DICT,
    EXAMPLE_ENGLISH_TOML_PATH,
    EXAMPLE_UNSUPPORTED_LANGUAGE_TOML_PATH,
)
from translation_library.utils.toml_utils import (
    deserialize_toml_dict,
    get_value_from_key,
    serialize_toml_dict,
)

# from glom.core import NonExistentKey  # type: ignore


def test_serialize_toml() -> None:
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT


def test_deserialize_toml() -> None:
    deserialize_toml_dict(EXAMPLE_ENGLISH_TOML_DICT, EXAMPLE_ENGLISH_TOML_PATH)
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT


def test_get_value_from_key_pass() -> None:
    get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="setting")


def test_get_value_from_key_nested_key_pass() -> None:
    get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="start.section_name")


def test_get_value_from_key_empty_path_fail() -> None:
    with pytest.raises(Exception):
        get_value_from_key("", key_path="hello")


def test_get_value_from_key_empty_key_path_fail() -> None:
    with pytest.raises(Exception):
        get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="")


def test_get_value_from_key_wrong_section_fail() -> None:
    with pytest.raises(Exception):
        get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="welcome")


def test_get_value_from_key_unsupported_language_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_value_from_key(EXAMPLE_UNSUPPORTED_LANGUAGE_TOML_PATH, key_path="hello")
