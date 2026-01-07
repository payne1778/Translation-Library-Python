from pathlib import Path

PARENT_DIR_PATH = Path(__file__).resolve().parent

EXAMPLE_UNSUPPORTED_LANGUAGE = "warlpiri"

EXAMPLE_SUPPORTED_LANGUAGE = "english"

EXAMPLE_UNSUPPORTED_LANGUAGE_TOML_PATH = Path(f"{EXAMPLE_UNSUPPORTED_LANGUAGE}.toml")

EXAMPLE_ENGLISH_TOML_PATH: Path = PARENT_DIR_PATH / "example.toml"

EXAMPLE_ENGLISH_TOML_DICT: dict = {
    "setting": "This is the English language file",
    "hello": "Hello {name}",
    "start": {
        "section_name": "This message is under the start section",
        "welcome": "Welcome {name}!",
    },
}
