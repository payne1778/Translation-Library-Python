from tests.utils.constants.values import (
    EXAMPLE_ENGLISH_TOML_DICT,
    EXAMPLE_ENGLISH_TOML_PATH,
)
from translation_library.utils.toml_utils import (
    deserialize_toml_dict,
    serialize_toml_dict,
)


def test_serialize_toml() -> None:
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT


def test_deserialize_toml() -> None:
    deserialize_toml_dict(EXAMPLE_ENGLISH_TOML_DICT, EXAMPLE_ENGLISH_TOML_PATH)
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT
