import operator
from enum import Enum


def contains(left, right) -> bool:
    """Same as ``left in right``"""
    return left in right


def truth(left, _) -> bool:
    """Same as ``bool(left) is True``"""
    return bool(left) is True


def null(left, _) -> bool:
    """Same as ``left is None``"""
    return left is None


def not_(left, _) -> bool:
    """Same as ``not left``"""
    return not left


class Operators(Enum):
    """
    Supported operators for asserting

    :return (operator_function, context, template_name)
    """
    JSON_EQUAL = operator.eq, 'equal to', 'JSON_EQUAL'  # a == b
    EQUAL = operator.eq, 'equal to', 'EQUAL'  # a == b
    NOT_EQUAL = operator.ne, 'not equal to', 'NOT_EQUAL',  # a != b
    GT = operator.gt, 'more than', 'GRATER'  # a > b
    LT = operator.lt, 'lower', 'LOWER'  # a < b
    LTE = operator.le, 'lower or equal', 'LOWER_OR_EQUAL'  # a <= b
    CONTAINS = contains, 'contains', 'CONTAINS'  # b in a
    NOT = not_, 'is not', 'NOT'  # not a
    TRUTH = truth, 'is truth', 'TRUTH'  # a is True (without checking type)
    NULL = null, 'is null', 'NULL'  # a is None
    STATUS_CODE = operator.eq, 'status code', 'STATUS_CODE',  # a == b
    ANY = any, 'matches any', 'ANY',
    ALL = all, 'matches all', 'ALL'
