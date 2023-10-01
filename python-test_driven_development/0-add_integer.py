#!/usr/bin/python3
"""
    Function that adds two numbers.
"""


def add_integer(a, b=98):
    """
        Returns the add of a, b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (a + b)
