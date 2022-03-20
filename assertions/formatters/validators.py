from enum import Enum


class AllureValidationTemplates(Enum):
    FOR_ARRAY = 'Checking that array with json {json} \n matches the schema {schema}'
    FOR_OBJECT = 'Checking that json {json} \n matches the schema {schema}'
