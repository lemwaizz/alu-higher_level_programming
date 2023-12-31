#!/usr/bin/python3
"""module for addition"""


def add_integer(a, b=98):
    """function for adding integers
       Args:
        a = must be an integer or a float
        b = must be an integer or a float as well. If not provided takes
        98 as a default value.
        if a is not integer raise a typeerror
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
