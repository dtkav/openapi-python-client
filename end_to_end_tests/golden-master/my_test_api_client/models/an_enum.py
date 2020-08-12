from enum import Enum


class AnEnum(str, Enum):
    FIRST_VALUE = "FIRST_VALUE"
    CAMELCASE = "camelCase"
    SORTASC = "sort:asc"
    TYPE = "type"
