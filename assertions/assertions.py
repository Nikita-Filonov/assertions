from http import HTTPStatus
from typing import Any, Union, Optional, List, Dict

import allure

from assertions.constants import TYPE_NAMES
from assertions.formatters.assertions import MessageTemplate, AllureTemplates
from assertions.operators import Operators
from assertions.utils import prettify_json


def compare_keys(a, b, keys):
    """
    :param a: {'id': 12345, 'name': 'Author'}
    :param b: {'id': 123456, 'name': 'Instructor'}
    :param keys: ['name']
    :return:

    Wrapper to map through all given ``keys`` and compare each of them
    """
    return all(a[key] == b[key] for key in keys)


def compare_with_left(b, left, keys):
    """
    :param keys:  ['name']
    :param b: {'name': 'Author'} from right
    :param left: [{'name': 'Author'}, {'name': 'Learner'}]
    :return:

    Wrapper to compare each element of ``right`` with ``left``
    """
    return any(compare_keys(a, b, keys) for a in left)


def compare_list_of_dicts(left: List[Dict], right: List[Dict], operator: Union[any, all], keys: List[str]) -> bool:
    """
    :param left: [{'id': 1, 'name': 'Author'}, {'id':2, 'name': 'Learner'}]
    :param right: [{'name': 'Author'}, {'name': 'Learner'}]
    :param operator: any or all
    :param keys: ['name'] - keys to compare
    :return: boolean result of comparing, result for same ``left``, ``right``
    might be different depends on ``operator``

    Example:
        >>> left_list = [{'id': 1, 'name': 'Author'}, {'id':2, 'name': 'Learner'}]
        >>> right_list = [{'name': 'Author'}, {'name': 'Learner'}]
        >>> some_keys = ['name']
        >>> op, _, _ = Operators.ALL.value
        >>> compare_list_of_dicts(left_list, right_list, op, some_keys)
        True
        >>> op, _, _ = Operators.ANY.value
        >>> compare_list_of_dicts(left_list, right_list, op, some_keys)
        True
    """
    return operator([compare_with_left(b, left, keys) for b in right])


def assert_(
        left: Union[HTTPStatus, dict, str, int, list, bool, None],
        right: Union[HTTPStatus, dict, str, int, list, bool, None] = None,
        what: str = '',
        operator: Operators = Operators.EQUAL,
        message: Optional[str] = None,
        allure_message: Optional[str] = None,
        keys: Optional[List[str]] = None
):
    """
    Base assertion function that can be used for asserting any ``SUPPORTED_TEMPLATES``.

    Why we need this?

    assert_(2, 3, 'some_id')
    This will produce AssertionError like:
    ``
    AssertionError: Checking that "some_id" = 2 equal to 3.
    2 is integer
    3 is integer
    ``

    Equivalent to:

    with allure.step('Checking that number "some_id" = 2 equal to 3.'):
         assert 2 == 3, 'Checking that number "some_id" = 2 equal to 3.'

    In seconds example problem is that we have to always write:
    with allure.step(...):
    but this not how we want to build our autotests, because some autotests
    may have 3 or maybe 15 checks, and we not going to write ``with allure.step(...)``
    for each check.

    1) So for the first point, we want to avoide always writing:
    with allure.step(...):

    2) For the Second point, we do not want to always write:
    assert 2 == 3, 'Checking that number "some_id" = 2 equal to 3.'
    assertion message for each check, for same reason, because autotests
    may have a lot of checks.

    3) Third point is that we want to have dynamic operator, like:
    assert 2 == 2
    assert 2 < 3
    assert 3 > 2

    ``assert_`` function also resolving this problem for us. All supported operators
    can be viewered in ``Operators`` class.

    4) Four point is that we want to see json like:
    {"id": 1, "name": "some", "active": true}
    instead of that we want to see:
    {
        "id": 1,
        "name": "some",
        "active": true
    }
    So we want to see pretified json, because it is better to understand.
    This function also resolving this problem.

    Example:
    Here you can see all common examples

    >>> assert_(True, what='user_id', operator=Operators.TRUTH)
    >>> assert_(None, what='user_id', operator=Operators.NULL)
    >>> assert_(5, 5, what='user_id', operator=Operators.EQUAL)
    >>> assert_('a', ['a'], what='user_id', operator=Operators.CONTAINS)
    >>> assert_(6, 5, what='user_id', operator=Operators.GT)
    >>> assert_(4, 5, what='user_id', operator=Operators.LT)
    >>> assert_(False, what='user_id', operator=Operators.NOT)
    >>> assert_(5, 6, what='user_id', operator=Operators.NOT_EQUAL)
    >>> assert_(200, HTTPStatus.OK, what='user_id', operator=Operators.STATUS_CODE)
    >>> assert_({"id": 1}, {"id": 1}, what='user_id', operator=Operators.EQUAL)
    """
    right_inst: Any = None if right is None else type(right)
    left_inst: Any = None if left is None else type(left)

    right_inst_name = TYPE_NAMES[right_inst]
    left_inst_name = TYPE_NAMES[left_inst]

    op, context, template = operator.value

    template_payload = {
        'left': left,
        'right': right,
        'context': context,
        'what': what,
        'right_inst': right_inst_name,
        'left_inst': left_inst_name
    }

    if isinstance(left, dict):
        template_payload = {**template_payload, 'left': prettify_json(left), 'right': prettify_json(right)}

    if isinstance(left, list) and all(isinstance(item, dict) for item in left):
        safe_left = [left[0]] if len(left) > 1 else left
        template_payload = {**template_payload, 'left': prettify_json(safe_left), 'right': prettify_json(right)}

    allure_template = AllureTemplates[template].value.format(**template_payload)
    message_template = MessageTemplate[template].value.format(**template_payload)

    with allure.step(allure_message or allure_template):
        if op in [any, all]:
            assert compare_list_of_dicts(left, right, op, keys), message or message_template
            return

        assert op(left, right), message or message_template
