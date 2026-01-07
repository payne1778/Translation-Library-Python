import logging
from os import walk
from os.path import exists
from pathlib import Path
from typing import Iterator, List, Tuple

from pydantic import Field, validate_call

logger = logging.getLogger(__name__)


def valid_path_validator(v: str | Path) -> Path:
    """
    Checks to see if a given path exists and whether it is of type `str`
    or `Path`.

    Args:
        v (str | Path): a supposed `str`/`Path` path to a file

    Raises:
        ValueError: if a `str`/`Path` path was given and is was None/null
        FileNotFoundError: if a `str`/`Path` path was given and it did not exist
        TypeError: if the arg was not of type `str` or `Path`

    Returns:
        Path: the original path if it exists, otherwise errors are raised.
    """
    if isinstance(v, str):
        if not v.strip():
            logger.error("arg '%s' was None/null", v)
            raise ValueError("file path cannot be None/null")
        elif not exists(Path(v)):
            logger.error("arg '%s' could not be located/does not exist", v)
            raise FileNotFoundError(f"path '{v}' could not be located/does not exist")
        return Path(v)

    if isinstance(v, Path):
        if v.as_posix().strip() is None:
            logger.error("arg '%s' was None/null", v)
            raise ValueError("file path cannot be None/null")
        elif not exists(v):
            logger.error("arg '%s' could not be located/does not exist", v)
            raise FileNotFoundError(f"path '{v}' could not be located/does not exist")
        return v

    logger.error("arg '%s' was not of type str or Path", v)
    raise TypeError("file path must be of type str or Path")


# def raise_for_nonexistence(file_path: str | Path) -> None:
#     """
#     Raises `FileNotFoundError` if the path from arg `file_path` does not exist

#     Args:
#         file_path (str | Path): the path of whose existence to check

#     Raises:
#         FileNotFoundError: if the path could not be located or does not exist
#     """
#     if not exists(file_path):
#         raise FileNotFoundError(f"'{file_path}' could not be located/does not exist")


@validate_call
def get_project_root(
    anchor: str = Field(default=".git", min_length=1),
) -> Path:
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
    logger.error("'anchor' arg '%s' was not in parents of %s", anchor, current_path)
    raise FileNotFoundError(
        f"Could not find '{anchor}' in the parent dirs of '{current_path}'"
    )


# TODO: find a way to check if language is supported
@validate_call
def get_language_file_path(language: str = Field(min_length=1)) -> Path:
    """
    Get the path of the TOML file for a specified language name.

    Args:
        language (str): the name of language whose TOML file path to retrieve

    Raises:
        FileNotFoundError: if the language's TOML file could not be found (ex. `english.toml`)

    Returns:
        Path: the absolute path of the specified language's TOML file
    """
    type Walker = Iterator[Tuple[str, List[str], List[str]]]
    walker: Walker = walk(get_project_root() / "lib")
    for dir_path, _, file_names in walker:
        for file_name in file_names:
            if file_name.lower() == f"{language.lower()}.toml":
                language_file_path: Path = Path(dir_path) / Path(file_name)
                logger.info("Successfuly found '%s'", language_file_path)
                return language_file_path

    logger.error("'%s.toml' could not be found", language)
    raise FileNotFoundError(f"Could not find the language TOML file for '{language}'")


def get_languages_file_path() -> Path:
    """
    Get the path of the TOML file that contains all supported languages.

    Raises:
        RuntimeError: if the languages TOML file, `languages.toml`, does not exist

    Returns:
        Path: the absolute path to `languages.toml`
    """
    try:
        # Uses get_language_file_path() to avoid code duplication.
        # Instead of `english.toml` or `german.toml`, it searches for `languages.toml`
        return get_language_file_path("languages")
    except FileNotFoundError:
        logger.error("'languages.toml' could not be found")
        raise FileNotFoundError("Could not find `languages.toml`")
