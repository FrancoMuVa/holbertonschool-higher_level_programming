#!/usr/bin/python3
"""
    Class Base: Represents the base class for all other classes in the
                project.
"""
import json


class Base():
    """
        Base class for managing id attribute in other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes a new instance of the Base class.

            Args:
                id (int): An optional ID value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
