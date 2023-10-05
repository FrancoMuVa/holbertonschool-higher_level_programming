#!/usr/bin/python3
"""
    Function that checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance, False otherwise. """
    return isinstance(obj, a_class) and not type(obj) is a_class
