#!/usr/bin/python3
"""
    Class Base Geometry.
"""


class BaseGeometry():
    """ Base Geometry """
    def area(self):
        """ Raise a exeption """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
