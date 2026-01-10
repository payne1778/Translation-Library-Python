from resources.constants.values import (
    EXAMPLE_SUPPORTED_LANGUAGE,
    EXAMPLE_UNSUPPORTED_LANGUAGE,
)
from translation_library.utils.language_utils import (
    get_languages,
    get_languages_as_english_names,
    get_value_from_language_toml,  # TODO: test this
    into_toml_dict,
    into_toml_str,
    is_supported,
)


def test_language_toml() -> None:
    assert isinstance(into_toml_dict(EXAMPLE_SUPPORTED_LANGUAGE), dict)


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


def test_into_toml_str() -> None:
    assert isinstance(into_toml_str(EXAMPLE_SUPPORTED_LANGUAGE), str)


# def test_get_value_from_language_toml() -> None:
#     assert (
#         get_value_from_language_toml(EXAMPLE_SUPPORTED_LANGUAGE, "hello")
#         == "Hello {name}"
#     )


# def test_get_value_from_language_toml() -> None:
#     assert (
#         get_value_from_language_toml(EXAMPLE_SUPPORTED_LANGUAGE, "hello")
#         == "Hello {name}"
#     )
