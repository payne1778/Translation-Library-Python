from tests.utils.constants.values import (
    EXAMPLE_SUPPORTED_LANGUAGE,
    EXAMPLE_UNSUPPORTED_LANGUAGE,
)
from translation_library.utils.language_utils import (
    get_languages,
    get_languages_anglicized,
    get_languages_toml_dict,
    into_toml_dict,
    is_supported,
)


def test_language_toml() -> None:
    assert isinstance(into_toml_dict(EXAMPLE_SUPPORTED_LANGUAGE), dict)


def test_languages_toml() -> None:
    assert isinstance(get_languages_toml_dict(), dict)


def test_get_languages() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE in get_languages()


def test_get_languages_anglicized() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE in get_languages_anglicized()


def test_is_supported_language() -> None:
    assert is_supported(EXAMPLE_SUPPORTED_LANGUAGE)


def test_is_supported_language_fail() -> None:
    assert not is_supported(EXAMPLE_UNSUPPORTED_LANGUAGE)
