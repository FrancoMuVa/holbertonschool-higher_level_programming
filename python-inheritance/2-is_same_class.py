#!/usr/bin/python3
"""
    Function that check if an object is exactly an instance of the
    specified class.
"""


def is_same_class(obj, a_class):
    """ Returns True if is an instance, False otherwise. """
    return type(obj) is a_class
