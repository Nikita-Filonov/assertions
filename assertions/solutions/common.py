from typing import Any, List, Dict

from assertions.assertions import assert_
from assertions.operators import Operators


def assert_truth(left: Any, what: str, **kwargs):
    """
    Can be used to check if value is truth, without type checking.

    Example:
        >>> my_value = [1, 2, 3]
        >>> assert_truth(my_value, 'my_value')

    """
    return assert_(left=left, what=what, operator=Operators.TRUTH, **kwargs)


def assert_not_truth(left: Any, what: str, **kwargs):
    """
    Can be used to check if value is truth, without type checking.

    Example:
        >>> my_value = []
        >>> assert_not_truth(my_value, 'my_value')

    """
    return assert_(left=left, what=what, operator=Operators.NOT, **kwargs)


def assert_all(left: List[Dict], right: List[Dict], what: str, keys: List[str], **kwargs):
    """
    Can be used to check if all values from left, equals to values from right by given keys

    Example:
        >>> my_value = [{'name': 1}, {'name': 2}, {'name': 3}]
        >>> api_response_value = [{'name': 1}, {'name': 2}, {'name': 3}]
        >>> assert_all(api_response_value, my_value, 'my_value', ['name'])
    """
    assert_(left=left, right=right, what=what, operator=Operators.ALL, keys=keys, **kwargs)


def assert_any(left: List[Dict], right: List[Dict], what: str, keys: List[str], **kwargs):
    """
    Can be used to check if some values from left, equals to values from right by given keys

    Example:
        >>> my_value = [{'name': 1}, {'name': 2}, {'name': 3}]
        >>> api_response_value = [{'name': 1}, {'name': 2}, {'name': 3}]
        >>> assert_any(api_response_value, my_value, 'my_value', ['name'])
    """
    assert_(left=left, right=right, what=what, operator=Operators.ANY, keys=keys, **kwargs)


def assert_lte(left, right, what, **kwargs):
    """
    Can be used to check if left is equal or lower than right

    Example:
        >>> left_value = 1
        >>> right_value = 2
        >>> assert_lte(left_value, right_value, 'My value count')
    """
    assert_(left=left, right=right, what=what, operator=Operators.LTE, **kwargs)
