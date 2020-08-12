import keyword
import re

import stringcase


def _shadow_keyword(value: str) -> str:
    """If the value is a keyword, append an underscore
    """
    if keyword.iskeyword(value):
        return f"{value}_"
    return value


def sanitize(value: str) -> str:
    """Sanitize value to be a valid python identifier

    Uses the following grammar:
    identifier ::=  (letter|"_") (letter | digit | "_")*
    letter     ::=  lowercase | uppercase
    lowercase  ::=  "a"..."z"
    uppercase  ::=  "A"..."Z"
    digit      ::=  "0"..."9"
    """
    if value.isidentifier():
        return _shadow_keyword(value)
    # Drop invalid characters
    value = re.sub("[^0-9a-zA-Z_]", "", value)
    # Drop invalid start characters
    value = re.sub("^[^a-zA-Z_]+", "", value)
    return _shadow_keyword(value)


def snake_case(value: str) -> str:
    value = re.sub(r"([A-Z]{2,})([A-Z][a-z]|[ -_]|$)", lambda m: m.group(1).title() + m.group(2), value.strip())
    value = re.sub(r"(^|[ _-])([A-Z])", lambda m: m.group(1) + m.group(2).lower(), value)
    return sanitize(stringcase.snakecase(value))


def pascal_case(value: str) -> str:
    return stringcase.pascalcase(value)


def spinal_case(value: str) -> str:
    return stringcase.spinalcase(value)
