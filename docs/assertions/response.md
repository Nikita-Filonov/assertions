Checks that can be used on the API response. For example, to check the status of the response code

assert_response_status
---
Used to check the status of the response code

```python
from http import HTTPStatus

from assertions import assert_response_status

actual_status_code = HTTPStatus.OK

assert_response_status(actual_status_code, HTTPStatus.OK)
```

assert_attr
---

Used to check a specific field in the response body

```python
from assertions import assert_attr

response_body = {
    'id': 1,
    'email': 'some@gmail.com',
    'username': 'username'
}

assert_attr(response_body['id'], 1, what='User id')
assert_attr(response_body['email'], 'some@gmail.com', what='User email')
```

assert_json
---

Used to check the whole json object

```python
from assertions import assert_json

actual_response_body = {
    'id': 1,
    'email': 'some@gmail.com',
    'username': 'username'
}
expected_response_body = {
    'id': 1,
    'email': 'some@gmail.com',
    'username': 'username'
}

assert_json(actual_response_body, expected_response_body)
```
