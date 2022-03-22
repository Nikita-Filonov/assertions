import logging
from typing import List

from assertions import assert_
from assertions.operators import Operators


def assert_model_equal(left: dict, right: dict, model, exclude: List[str] = None):
    """
    :param left: Any json
    :param right: Any json
    :param model: Any json model we want to check
    :param exclude: List of fields which we want to exclude from checking
    :raises: AssertionError if some of left value does not equal right value
    """
    missing_keys = []
    safe_left = dict(filter(lambda field: field[0] not in (exclude or []), left.items()))

    model_fields = model.manager.fields(json_key=True)
    for key, value in safe_left.items():
        if key not in right.keys():
            missing_keys.append(key)
            continue

        assert_(left=value, right=right[key], what=model_fields[key].json, operator=Operators.EQUAL)

    if missing_keys:
        logging.warning(f'Unable to find keys {", ".join(missing_keys)} in {right}, checking "{model.__name__}"')
