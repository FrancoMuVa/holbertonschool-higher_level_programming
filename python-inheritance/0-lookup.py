#!/usr/bin/python3
"""
    Function that returns a list of all attributes and methods of an objects.
"""


def lookup(obj):
    """ Returns a list of attributes and methods of an objects

        Args:
            obj (object): Return a list of attributes and methods of obj.
    """
    return dir(obj)
