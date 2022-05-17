These checks are mostly related to model created with models-manager

assert_model_equal
---

Used to compare the fields of one json object with another json object. In this case, the validation will be based on
the fields of the model. This can be used for example when you create an entity with specific json. And in the response
you expect the same entity with the same json

```python
from models_manager import Model, Field

from assertions import assert_model_equal


class User(Model):
    id = Field(json='id', category=int, default=1)
    username = Field(json='username', category=str, default='some')


actual_payload = {
    'id': 1,
    'username': 'some'
}
response_payload = {
    'id': 1,
    'username': 'some'
}

assert_model_equal(actual_payload, response_payload, User)
```

In this case, the check will go through all the model fields of the expected json object and compare it with the object
received from the API response. Nested entities are not currently supported
