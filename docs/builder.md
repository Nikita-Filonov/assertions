The builder function or `assert_` allows us to write absolutely any checks.

Arguments:

- `left` - actual result
- `right` - expected result
- `what` - any human-readable string which should describe what are you asserting
- `operator` - operator type of `Operators`, which will be used to compare values
- `message` - optional error message, which will be shown when error raised
- `allure_message` - optional allure step message, which will be used for allure step
- `keys` - used only for certain assert solutions. Ref to [assert_all](./assertions/common.md#assert_all),
  [assert_any](./assertions/common.md#assert_any)

Example of `assert_` usage

```python
from assertions import assert_, Operators

assert_(4, 4, 'Some equal numbers', Operators.EQUAL)
assert_(4, 5, 'Some lte numbers', Operators.LTE)
assert_(4, 5, 'Some not equal numbers', Operators.NOT_EQUAL)
```
