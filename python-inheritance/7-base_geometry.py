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
        if isinstance(name, str):    
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
