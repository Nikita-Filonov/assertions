from enum import Enum


class AllureTemplates(Enum):
    STATUS_CODE = 'Checking that response status code equals to {right}.'
    TRUTH = 'Checking that "{what}" is truth.'
    NULL = 'Checking that "{what}" is null.'
    EQUAL = 'Checking that "{what}" equal to {left}.'
    CONTAINS = 'Checking that "{what}" equal to {left} is contained in {right}.'
    GRATER = 'Checking that "{what}" equal to {left} more that {right}.'
    LOWER = 'Checking that "{what}" equal to {left} lower than {right}.'
    LOWER_OR_EQUAL = 'Checking that "{what}" equal to {left} lower than or equal {right}.'
    NOT = 'Checking that "{what}" equal to {left} is not true.'
    NOT_EQUAL = 'Checking that "{what}" not equal to {right}.'
    JSON_EQUAL = 'Checking that response json {left} \nequal to {right}.'
    ANY = 'Checking that "{what}" equal to {left} matches any of {right}.'
    ALL = 'Checking that "{what}" equal to {left} matches all of {right}.'


class MessageTemplate(Enum):
    STATUS_CODE = 'Checking that response status code equals to {right}({right_inst}). ' \
                  'But actually it equals {left}({left_inst}).'
    TRUTH = 'Checking that "{what}" is truth. But actually it equals {left}({left_inst}).'
    NULL = 'Checking that "{what}" is null. But actually it equals {left}({left_inst}).'
    EQUAL = 'Checking that "{what}" equal to {left}({left_inst}). But actually it equals {right}({right_inst}).'
    CONTAINS = 'Checking that "{what}" equal to {left}({left_inst}) is contained in {right}({right_inst}).'
    GRATER = 'Checking that "{what}" equal to {left}({left_inst}) more that {right}({right_inst}).'
    LOWER = 'Checking that "{what}" equal to {left}({left_inst}) lower than {right}({right_inst}).'
    LOWER_OR_EQUAL = 'Checking that "{what}" equal to {left}({left_inst}) lower than or equal {right}({right_inst}).'
    NOT = 'Checking that "{what}" equal to {left}({left_inst}) is not true'
    NOT_EQUAL = 'Checking that "{what}" not equal to {right}({right_inst}). ' \
                'But actually it equals {left}({left_inst}).'
    JSON_EQUAL = 'Checking that response json {left} \nequal to {right}.'
    ANY = 'Checking that "{what}" equal to {left}({left_inst}) matches any of {right}({right_inst}).'
    ALL = 'Checking that "{what}" equal to {left}({left_inst}) matches all of {right}({right_inst}).'
