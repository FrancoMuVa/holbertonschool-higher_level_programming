#!/usr/bin/python3
"""
    Save to json file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
        Function that writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(json.dumps(my_obj))
