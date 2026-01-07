import logging

from translation_library.utils.language_utils import (
    get_languages,
    get_languages_anglicized,
    get_value_from_language_toml,
    local_get_language_file_path,
    print_toml_dict,
)
from translation_library.utils.path_utils import valid_path_validator

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # variable: str = "hello"
    # section: str = ""
    # variable_args: dict[str, object] = {"name": "Bob"}

    # message_string = ""
    # toml_dict = language_toml("english")

    # if not section and not variable_args:
    #     message_string = toml_dict[variable]
    # elif section and not variable_args:
    #     message_string = toml_dict[section][variable]
    # elif not section and variable_args:
    #     message_string = toml_dict[variable].format(**variable_args)
    # else:
    #     message_string = toml_dict[section][variable].format(**variable_args)

    # print("TRANSLATION: " + message_string)
    # get_values_from_key("english", "hello")

    logger.debug("Starting session")

    # print(get_value_from_language_toml("german", "start.welcome"))
    # print(get_languages())
    # print(get_languages_anglicized())
    # print_toml_dict("english")

    valid_path_validator(local_get_language_file_path("en"))
    valid_path_validator(local_get_language_file_path("de"))

    logger.debug("Ending session")
