# mypy: ignore-errors

import logging
from pathlib import Path

from translation_library.utils.path_utils import get_project_root
from translation_library.utils.toml_utils import get_value_from_key

logger = logging.getLogger(__name__)


def get_config_file_path() -> Path:
    return get_project_root() / "config.toml"


def get_value_from_config(key_path: str) -> str | list[str] | list[dict[str, object]]:
    return get_value_from_key(get_config_file_path(), key_path)


def get_i18n_dir_path() -> Path:
    return get_project_root() / Path(str(get_value_from_config("paths.i18n_dir")))


def get_all_english_names() -> list[str]:
    return list(get_value_from_config(f"languages.*.english_name"))


def get_all_native_names() -> list[str]:
    return list(get_value_from_config(f"languages.*.native_name"))


def language_code_to_english_name(code: str) -> str:
    return str(get_value_from_config(f"languages.{code.lower()}.english_name"))


def language_code_to_native_name(code: str) -> str:
    return str(get_value_from_config(f"languages.{code.lower()}.native_name"))


# TODO: make this return language code
def native_name_to_language_code(name: str) -> str:
    for language in get_value_from_config(f"languages.*"):
        if name.lower() == language["native_name"].lower():
            return language["native_name"]
    raise ValueError(f"native name '{name}' was not in config file")


# TODO: make this return language code
def english_name_to_language_code(name: str) -> str:
    for language in get_value_from_config(f"languages.*"):
        if name.lower() == language["english_name"].lower():
            return language["english_name"]
    raise ValueError(f"english name '{name}' was not in config file")


def get_language_file_path(code: str) -> Path:
    return get_i18n_dir_path() / Path(
        str(get_value_from_config(f"languages.{code.lower()}.file"))
    )
