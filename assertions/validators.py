from typing import Union

import allure
from jsonschema import validate

from assertions.formatters.validators import AllureValidationTemplates
from assertions.utils import prettify_json


def validate_json(json: Union[dict, list], schema: dict):
    """
    Used to validate json schema.

    You can get schema by using .to_schema method of model manager
    Example:
    >>> some_json = {"id": 1, "name": "string"}
    >>> some_schema = {
    ...     "type": "object",
    ...     "properties": {
    ...         "id": {"type": "number"},
    ...         "name": {"type": "string"}
    ...     }
    ... }

    # If no exception is raised by validate(), the instance is valid.
    >>> validate_json(json=some_json, schema=some_schema)
    """
    template_payload = {
        'json': prettify_json(json),
        'schema': prettify_json(schema),
        'template': AllureValidationTemplates.FOR_OBJECT
    }

    if isinstance(json, list) and len(json) >= 1:
        template_payload = {
            **template_payload,
            'json': prettify_json([json[0]]),
            'template': AllureValidationTemplates.FOR_ARRAY
        }

    allure_message = template_payload['template'].value.format(**template_payload)

    with allure.step(allure_message):
        validate(instance=json, schema=schema)
