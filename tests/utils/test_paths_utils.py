from pathlib import Path

import pytest

from translation_library.utils.path_utils import (
    get_language_file_path,
    get_languages_file_path,
    get_project_root,
    raise_for_nonexistance,
)

PARENT_DIR_PATH = Path(__file__).resolve().parent

EXAMPLE_ENGLISH_TOML_PATH: Path = PARENT_DIR_PATH / "example_english.toml"


def test_raise_for_nonexistance() -> None:
    raise_for_nonexistance(EXAMPLE_ENGLISH_TOML_PATH)


def test_raise_for_nonexistance_fail() -> None:
    with pytest.raises(FileNotFoundError):
        raise_for_nonexistance(PARENT_DIR_PATH / "warlpiri.toml")


def test_get_project_root() -> None:
    assert get_project_root().exists()


def test_get_language_file_path() -> None:
    assert get_language_file_path("english").exists()


def test_get_language_file_path_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_language_file_path("warlpiri")


def test_get_languages_file_path() -> None:
    assert get_languages_file_path().exists()
