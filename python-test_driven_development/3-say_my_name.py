#!/usr/bin/python3
"""
    Function that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name:

        Args:
            first_name (str): The first name.
            last_name (str, Nothing): The last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("{} {}".format(first_name, last_name))
