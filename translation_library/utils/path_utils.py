from os import walk
from os.path import join
from pathlib import Path
from typing import Iterator, List, Tuple

type Walker = Iterator[Tuple[str, List[str], List[str]]]


def get_project_root(anchor_file=".git") -> Path:
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / anchor_file).exists():
            return parent
    raise FileNotFoundError(
        f"Could not find '{anchor_file}' in the parent dirs of '{current_path}'"
    )


def get_language_file_path(language: str) -> Path:
    walker: Walker = walk(join(get_project_root() / "lib"))
    for dir_path, dir_names, file_names in walker:
        for file_name in file_names:
            if file_name == f"{language.lower()}.toml":
                return Path(dir_path) / Path(file_name)

    raise FileNotFoundError(f"Could not find the language file for '{language}'")


def get_languages_file_path() -> Path:
    try:
        return get_language_file_path("languages")
    except FileNotFoundError:
        raise RuntimeError("Languages TOML file does not exist")
