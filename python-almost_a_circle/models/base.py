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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Class method that writes the JSON string representation
            of list_objs to a file.
        """
        dict_objs = []
        for item in list_objs:
            dict_objs.append(item.to_dictionary())

        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="UTF8") as f:
            f.write(cls.to_json_string(dict_objs))

    @staticmethod
    def from_json_string(json_string):
        """
            Static method that returns the list
            of the JSON string representation json_string
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Class method  that returns an instance
            with all attributes already set.
        """
        if cls.__name__ == "Rectangle" or cls.__name__ == "Square":
            instance = cls(2, 2)
        else:
            return None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
            Class method that returns a list of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="UTF8") as f:
                read_file = f.read()
                list_objs = cls.from_json_string(read_file)
                create_return = []
                for item in list_objs:
                    create_return.append(cls.create(**item))
                return create_return
        except FileNotFoundError:
            return []
