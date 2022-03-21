# Pytest Assertions

Scope of assertions methods, which provides simple interface for creating checks in autotests

### Examples

```python
from http import HTTPStatus

from assertions import assert_
from assertions.operators import Operators

assert_(True, what='user_id', operator=Operators.TRUTH)
assert_(None, what='user_id', operator=Operators.NULL)
assert_(5, 5, what='user_id', operator=Operators.EQUAL)
assert_('a', ['a'], what='user_id', operator=Operators.CONTAINS)
assert_(6, 5, what='user_id', operator=Operators.GT)
assert_(4, 5, what='user_id', operator=Operators.LT)
assert_(False, what='user_id', operator=Operators.NOT)
assert_(5, 6, what='user_id', operator=Operators.NOT_EQUAL)
assert_(200, HTTPStatus.OK, what='user_id', operator=Operators.STATUS_CODE)
assert_({"id": 1}, {"id": 1}, what='user_id', operator=Operators.EQUAL)
```

### Build in solutions

```python
from assertions import assert_all, assert_any, assert_lte

my_value = [{'name': 1}, {'name': 2}, {'name': 3}]
api_response_value = [{'name': 1}, {'name': 2}, {'name': 3}]

assert_all(api_response_value, my_value, 'my_value', ['name'])
assert_any(api_response_value, my_value, 'my_value', ['name'])

left_value = 1
right_value = 2
assert_lte(left_value, right_value, 'My value count')
```

Full list of solutions

```
assert_
assert_all
assert_any
assert_lte
assert_truth
assert_attr
assert_json
assert_response_status
assert_model_equal
validate_json
```
