"""
HTTP response assertions wrappers over base ``_assert`` method
"""

from typing import Any

from assertions.assertions import assert_
from assertions.operators import Operators


def assert_response_status(left: int, right: int, **kwargs):
    """
    Can be used to check http response status code.

    Example:
    >>>from http import HTTPStatus
    >>>status_code = 200
    >>>assert_response_status(status_code, HTTPStatus.OK)
    """
    return assert_(left=left, right=right, operator=Operators.STATUS_CODE, **kwargs)


def assert_attr(left: Any, right: Any, what: str, **kwargs):
    """
    Can be used to check any attrs like: strings, integers, lists, dicts etc.

    Example:
    >>>actual_user_id = 'some_id'
    >>>expected_user_id = 'some_id'
    >>>assert_attr(actual_user_id, expected_user_id, 'user_id')
    """
    return assert_(left=left, right=right, what=what, operator=Operators.EQUAL, **kwargs)


def assert_json(left: dict, right: dict, **kwargs):
    """
    Can be used to check any json objects, in python called dicts

    Example:
    >>>actual_json = {'id': 'some_id'}
    >>>expected_json = {'id': 'some_id'}
    >>>assert_json(actual_json, expected_json)
    """
    return assert_(left=left, right=right, operator=Operators.JSON_EQUAL, **kwargs)
