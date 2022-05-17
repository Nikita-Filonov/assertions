Scope of assertions methods, which provides simple interface for creating checks in autotests The main purpose of this
library is to add generalization to allure steps, and to composing checks, as well as errors. When all checks look the
same, they are better read and understood.

This library uses pattern assert matches/objects. Which tells us that we should abstract our checks so that we don't
have to duplicate them in the future. That is, if we have a check for the status of the response code, then we take it
out into a separate function that will serve as this abstraction. Also, this pattern significantly increases the
readability of the code.
