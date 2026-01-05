import pytest

from translation_library.utils.path_utils import (
    get_language_file_path,
    get_languages_file_path,
    get_project_root,
)


def test_get_project_root() -> None:
    assert get_project_root().exists()


def test_get_language_file_path() -> None:
    assert get_language_file_path("english").exists()


def test_get_language_file_path_fail() -> None:
    with pytest.raises(FileNotFoundError):
        get_language_file_path("warlpiri")


def test_get_languages_file_path() -> None:
    assert get_languages_file_path().exists()
