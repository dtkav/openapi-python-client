from enum import Enum


class AnEnum(str, Enum):
    FIRST_VALUE = "FIRST_VALUE"
    SECOND_VALUE = "SECOND-VALUE"
    THIRD_VALUE_ASC = "THIRD_VALUE:ASC"
