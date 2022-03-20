from itertools import zip_longest
from typing import List

from assertions.assertions import assert_
from assertions.operators import Operators


def normalize_model_json(model_json: dict, exclude: List[str]) -> dict:
    """
    Can be used to normalize model json
    - Sort by key property
    - Exclude key from ``exclude`` list
    """
    sorted_model_json = dict(sorted(model_json.items()))
    return dict(filter(lambda field: field[0] not in exclude, sorted_model_json.items()))


def assert_model_equal(left: dict, right: dict, model, exclude: List[str] = None):
    """
    :param left: Any json
    :param right: Any json
    :param model: Any json model we want to check
    :param exclude: List of fields which we want to exclude from checking
    :raises: AssertionError if some of left value does not equal right value
    """
    safe_exclude = [*(exclude or []), 'tenant']
    safe_left = normalize_model_json(left, safe_exclude)
    safe_right = normalize_model_json(right, safe_exclude)

    model_fields = model.manager.fields(json_key=True)
    for (left_key, left_value), (_, right_value) in zip_longest(safe_left.items(), safe_right.items()):
        assert_(left=left_value, right=right_value, what=model_fields[left_key].json, operator=Operators.EQUAL)
