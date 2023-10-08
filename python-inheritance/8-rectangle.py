#!/usr/bin/python3
"""
    class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle """

    def __init__(self, width, height):
        """
            Initialize a Rectangle object
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
