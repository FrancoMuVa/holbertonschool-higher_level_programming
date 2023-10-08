#!/usr/bin/python3
"""
    Class Square that inherits from Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        Squere class
    """
    def __init__(self, size):
        """
            Initialize a Squere object
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
            Calculate the area of Square
        """
        return (self.__size * self.__size)
