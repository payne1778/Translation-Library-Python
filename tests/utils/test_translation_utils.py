from resources.constants.values import (
    EXAMPLE_SUPPORTED_LANGUAGE,
    EXAMPLE_UNSUPPORTED_LANGUAGE,
)
from translation_library.utils.translation_utils import (
    get_i18n_obj,  # TODO: test this
    get_languages,
    get_languages_as_english_names,
    is_supported,
)


def test_get_languages() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE in get_languages()


def test_get_languages_fail() -> None:
    assert EXAMPLE_UNSUPPORTED_LANGUAGE not in get_languages()


def test_get_languages_as_english_names() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE in get_languages_as_english_names(lowercase=True)


def test_get_languages_as_english_names_fail() -> None:
    assert EXAMPLE_UNSUPPORTED_LANGUAGE not in get_languages_as_english_names(
        lowercase=True
    )


def test_is_supported_language() -> None:
    assert is_supported(EXAMPLE_SUPPORTED_LANGUAGE)


def test_is_supported_language_fail() -> None:
    assert not is_supported(EXAMPLE_UNSUPPORTED_LANGUAGE)
