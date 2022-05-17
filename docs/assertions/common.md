General checks that can be used to check anything

assert_truth
---
Used to check if an object is True

```python
from assertions import assert_truth

assert_truth([1, 2, 3], what='My array with integers')
assert_truth(0, what='My integer')
```

assert_not_truth
---

Used to check if an object is not True

```python
from assertions import assert_not_truth

assert_not_truth([1, 2, 3], what='My array with integers')
assert_not_truth(0, what='My integer')
```

assert_all
---

Used to compare two lists with objects. This method will iterate through each of the lists and compare the corresponding
element with another. Expected that **all** values from actual, will equal to expected. Same as python `all` function.

!!! note

    It is worth noting that when checking lists, sorting may not match. That is, if two lists have different sorting 
    of elements, then the method will sort them and after that asserting will occur. This is true for `all`, `any`

```python
from assertions import assert_all

actual = [
    {'id': 1, 'name': 'some'},
    {'id': 2, 'name': 'other'},
    {'id': 3, 'name': 'another'}
]

expected = [
    {'id': 1, 'name': 'some'},
    {'id': 2, 'name': 'other'},
    {'id': 3, 'name': 'another'}
]

assert_all(actual, expected, keys=['name'], what='List of my dictionaries')
```

assert_any
---

Used to compare two lists with objects. This method will iterate through each of the lists and compare the corresponding
element with another. Expected that **any** values from actual, will equal to expected. Same as python `any` function.

This will not raise an `AssertionError`

```python
from assertions import assert_any

actual = [
    {'id': 1, 'name': 'some12345'},
    {'id': 2, 'name': 'other12345'},
    {'id': 3, 'name': 'another'}
]

expected = [
    {'id': 1, 'name': 'some'},
    {'id': 2, 'name': 'other'},
    {'id': 3, 'name': 'another'}
]

assert_any(actual, expected, keys=['name'], what='List of my dictionaries')
```

But in this case `AssertionError` will be raised

```python
from assertions import assert_any

actual = [
    {'id': 1, 'name': 'some12345'},
    {'id': 2, 'name': 'other12345'},
    {'id': 3, 'name': 'another12345'}
]

expected = [
    {'id': 1, 'name': 'some'},
    {'id': 2, 'name': 'other'},
    {'id': 3, 'name': 'another'}
]

assert_any(actual, expected, keys=['name'], what='List of my dictionaries')
```

assert_lte
---
Can be used to check if left is equal or lower than right

```python
from assertions import assert_lte

actual_items = 5
expected_items = 6

assert_lte(actual_items, expected_items, what='Number of items')
```

assert_contains
---
Can be used to check if some object contains item

```python
from assertions import assert_contains

items = [1, 2, 3, 4, 5]

assert_contains(items, 1, 'Item')
assert_contains(items, 10, 'Item')
```
