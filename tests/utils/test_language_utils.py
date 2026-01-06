from translation_library.utils.language_utils import (
    get_languages,
    get_languages_anglicized,
    is_supported_language,
    language_toml,
    languages_toml,
)


def test_language_toml() -> None:
    assert isinstance(language_toml("english"), dict)


def test_languages_toml() -> None:
    assert isinstance(languages_toml(), dict)


def test_get_languages() -> None:
    assert "English" in get_languages()


def test_get_languages_anglicized() -> None:
    assert "english" in get_languages_anglicized()


def test_is_supported_language() -> None:
    assert is_supported_language("english")


def test_is_supported_language_fail() -> None:
    assert not is_supported_language("warlpiri")
