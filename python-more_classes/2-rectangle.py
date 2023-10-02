#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty Class """

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of Rectangle

            Args:
                width (int, optional): The width of Rectangle.
                height (int, optional): The height of Rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """ Retrieve the value height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the value height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Retrieve the value width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the value width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Returns the area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of Rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)
