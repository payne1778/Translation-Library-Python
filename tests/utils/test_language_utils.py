from resources.constants.values import EXAMPLE_SUPPORTED_LANGUAGE
from translation_library.utils.language_utils import into_toml_dict, into_toml_str


def test_language_toml() -> None:
    assert isinstance(into_toml_dict(EXAMPLE_SUPPORTED_LANGUAGE), dict)


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
