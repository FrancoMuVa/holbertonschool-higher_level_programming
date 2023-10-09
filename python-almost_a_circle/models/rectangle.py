#!/usr/bin/python3
"""
    Rectangle Module: Defines the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
         Rectangle class inherits from Base.
        Represents a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
             Initializes a new instance of the Rectangle class.

            Args:
                width:  (int) The width of rectangle.
                heigth: (int) The height of the rectangle.
                x:      (int, optional) The x coordinate.
                y:      (int, optional) The x coordinate.
                id:     (int, optional) The ID value.
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter for the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute. """
        self.__width = value

    @property
    def height(self):
        """  Getter for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute. """
        self.__height = value

    @property
    def x(self):
        """  Getter for the x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute. """
        self.__x = value

    @property
    def y(self):
        """  Getter for the y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute. """
        self.__y = value
