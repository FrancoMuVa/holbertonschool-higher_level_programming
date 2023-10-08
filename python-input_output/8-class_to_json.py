#!/usr/bin/python3
"""
    Class ro json
"""


def class_to_json(obj):
    """
        Function that returns the dictionary description with simple
        data structure for JSON serialization of an object.
    """
    dict_obj = obj.__dict__

    for key, value in dict_obj.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dict_obj[key] = value
    return dict_obj
