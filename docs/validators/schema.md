These functions are used to validate the schema. The schema can be generated either by hand or with the help of a third
party library such as models-manager

Consider a simple example for schema validation

```python
from assertions import validate_json

some_json = {
    'id': 1,
    'email': 'som@gmail.com',
    'isActive': True
}
some_json_schema = {
    'title': 'SomeObject',
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'email': {'type': 'string'},
        'isActive': {'type': 'boolean'}
    },
    'required': ['id', 'email', 'isActive']
}

validate_json(json=some_json, schema=some_json_schema)
```

In this example, the result will be positive and the validation will be successful. Let's look at what happens if we run
validation on a non-valid json object

```python hl_lines="4"
from assertions import validate_json

some_json = {
    'id': {'error': 'Could not load user id'},
    'email': 'som@gmail.com',
    'isActive': True
}
some_json_schema = {
    'title': 'SomeObject',
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'email': {'type': 'string'},
        'isActive': {'type': 'boolean'}
    },
    'required': ['id', 'email', 'isActive']
}

validate_json(json=some_json, schema=some_json_schema)
```

If we execute the example above, we get the following validation error

```
jsonschema.exceptions.ValidationError: {'error': 'Could not load user id'} is not of type 'number'

Failed validating 'type' in schema['properties']['id']:
    {'type': 'number'}

On instance['id']:
    {'error': 'Could not load user id'}
```
