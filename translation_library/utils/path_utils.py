from os import walk
from os.path import exists
from pathlib import Path
from typing import Iterator, List, Tuple

type Walker = Iterator[Tuple[str, List[str], List[str]]]


def raise_for_nonexistance(file_path: str | Path) -> None:
    """
    Raises `FileNotFoundError` if the path from arg `file_path` does not exist

    Args:
        file_path (str | Path): the path of whose existance to check

    Raises:
        FileNotFoundError: if the path could not be located or does not exist
    """
    if not exists(file_path):
        raise FileNotFoundError(f"'{file_path}' could not be located/does not exist")


def get_project_root(anchor=".git") -> Path:
    """
    Find and return the path of the root path of the project.

    Args:
        anchor (str, optional): a known file/dir that exists in the project root. Defaults to ".git".

    Raises:
        FileNotFoundError: if `anchor` could not be found in parent dirs

    Returns:
        Path: the path of the project root
    """
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / anchor).exists():
            return parent
    raise FileNotFoundError(
        f"Could not find '{anchor}' in the parent dirs of '{current_path}'"
    )


def get_language_file_path(language: str) -> Path:
    """
    Get the path of the TOML file for a specified language name.

    Args:
        language (str): the name of language whose TOML file path to retrieve

    Raises:
        FileNotFoundError: if the language's TOML file could not be found (ex. `english.toml`)

    Returns:
        Path: the absoulte path of the specified language's TOML file
    """
    walker: Walker = walk(get_project_root() / "lib")
    for dir_path, _, file_names in walker:
        for file_name in file_names:
            if file_name == f"{language.lower()}.toml":
                return Path(dir_path) / Path(file_name)

    raise FileNotFoundError(f"Could not find the language file for '{language}'")


def get_languages_file_path() -> Path:
    """
    Get the path of the TOML file that contains all supported languages.

    Raises:
        RuntimeError: if the languages TOML file, `languages.toml`, does not exist

    Returns:
        Path: the absoulte path to `languages.toml`
    """
    try:
        # Uses get_language_file_path() to avoid code duplication.
        # Instead of `english.toml` or `german.toml`, it searches for `languages.toml`
        return get_language_file_path("languages")
    except FileNotFoundError:
        raise FileNotFoundError("Could not find `languages.toml`")
