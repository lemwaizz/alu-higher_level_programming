#!/usr/bin/python3
def add_integer(a, b=98):
    """function for adding integers
       Args:
        a = must be an integer or a float
        b = must be an integer or a float as well. If not provided takes 98 as a default value.
        if a is not integer raise a typeerror
    """
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(a) != int:
        raise TypeError("b must be an integer")
    if type(a) == int and type(b) == int:
        return a + b
    elif type(a) == float or type(b) == float:
        a_1 = int(a)
        b_1 = int(b)
        return a_1 + b_1
