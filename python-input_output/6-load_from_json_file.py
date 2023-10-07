#!/usr/bin/python3
"""
    Load from json file.
"""
import json


def load_from_json_file(filename):
    """  Function that creates an Object from a “JSON file” """
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
