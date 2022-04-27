General checks that can be used to check anything

assert_truth
---
Used to check if an object is True

| name  | value      | description |
| :---- | :--------- | :---- |
| left  | Any object | Object which we want ensure that is `True` |
| what  | Any string | Any human readable string, for describing what are we checking |

```python
from assertions import assert_truth

assert_truth([1, 2, 3], what='My array with integers')
assert_truth(0, what='My integer')
```

assert_not_truth
---

Used to check if an object is not True

| name  | value      | description |
| :---- | :--------- | :---- |
| left  | Any object | Object which we want ensure that is `True` |
| what  | Any string | Any human readable string, for describing what are we checking |

```python
from assertions import assert_not_truth

assert_not_truth([1, 2, 3], what='My array with integers')
assert_not_truth(0, what='My integer')
```

assert_all
---

Used to compare two lists with objects. This method will iterate through each of the lists and compare the corresponding
element with another

| name  | value      | description |
| :---- | :--------- | :---- |
| left  | Any object | Object which we want ensure that is `True` |
| right  | Any object | Object which we want ensure that is `True` |
| keys  | List strings | List of keys to check |
| what  | Any string | Any human readable string, for describing what are we checking |

assert_any
---

assert_lte
---
