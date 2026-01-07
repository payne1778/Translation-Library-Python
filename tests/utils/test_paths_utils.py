from pathlib import Path

import pytest

from tests.utils.constants.values import (
    EXAMPLE_ENGLISH_TOML_PATH,
    EXAMPLE_SUPPORTED_LANGUAGE,
    EXAMPLE_UNSUPPORTED_LANGUAGE,
)
from translation_library.utils.path_utils import (
    get_language_file_path,
    get_languages_file_path,
    get_project_root,
    valid_path_validator,
)


def test_valid_path_validator() -> None:
    valid_path_validator(EXAMPLE_ENGLISH_TOML_PATH)


def test_valid_path_validator_empty_str_fail() -> None:
    with pytest.raises(ValueError):
        valid_path_validator("")


def test_valid_path_validator_nonexistant_str_path_fail() -> None:
    with pytest.raises(FileNotFoundError):
        valid_path_validator(f"{EXAMPLE_UNSUPPORTED_LANGUAGE}.toml")


def test_valid_path_validator_nonexistant_path_fail() -> None:
    with pytest.raises(FileNotFoundError):
        valid_path_validator(Path(f"{EXAMPLE_UNSUPPORTED_LANGUAGE}.toml"))


def test_get_project_root() -> None:
    assert get_project_root().exists()


def test_get_project_root_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_project_root(anchor=f"{EXAMPLE_UNSUPPORTED_LANGUAGE}.toml")


def test_get_language_file_path() -> None:
    assert get_language_file_path(EXAMPLE_SUPPORTED_LANGUAGE).exists()


def test_get_language_file_path_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_language_file_path(EXAMPLE_UNSUPPORTED_LANGUAGE)


def test_get_languages_file_path() -> None:
    assert get_languages_file_path().exists()
