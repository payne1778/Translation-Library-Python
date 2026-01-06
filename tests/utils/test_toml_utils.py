from pathlib import Path

from translation_library.utils.toml_utils import (
    deserialize_toml_dict,
    serialize_toml_dict,
)

PARENT_DIR_PATH = Path(__file__).resolve().parent

EXAMPLE_ENGLISH_TOML_PATH: Path = PARENT_DIR_PATH / "example_english.toml"

EXAMPLE_ENGLISH_TOML_DICT: dict = {
    "setting": "This is the English language file",
    "hello": "Hello {name}",
    "start": {
        "section_name": "This message is under the start section",
        "welcome": "Welcome {name}!",
    },
}


def test_serialize_toml() -> None:
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT


def test_deserialize_toml() -> None:
    deserialize_toml_dict(EXAMPLE_ENGLISH_TOML_DICT, EXAMPLE_ENGLISH_TOML_PATH)
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT
