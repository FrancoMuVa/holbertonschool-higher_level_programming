#!/usr/bin/python3
"""
    Function that adds two numbers.
"""


def add_integer(a, b=98):
    """
        Returns the add of a, b
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
