from translation_library.utils.language_utils import language_toml_dict
from translation_library.utils.toml_utils import get_value_from_key

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

    print(get_value_from_key("english", "description"))
