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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""
    class Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """ Rectangle """

    def __init__(self, width, height):
        """ Initialize a Rectangle object """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculate the area """
        return self.__width * self.__height

    def __str__(self):
        """ Return a string representation of Rectangle """
        return f"[Rectangle] { self.__width}/{self.__height}"


"""
    Class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """ Squere """

    def __init__(self, size):
        """ Initialize a Squere object """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Calculate the area of Square """
        return self.__size * self.__size
