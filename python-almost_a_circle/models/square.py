#!/usr/bin/python3
"""
    Square Module: Defines the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class inherits from Rectangle.
        Reprecents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes a new instance of the Square class.

            Args:
                size: (int) The size of a side of the square.
                x:    (int, optional) The x coordinate.
                y:    (int, optional) The y coordinate.
                id:   (int, optional) The ID value.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for the width attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the size attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string reprecentation of Square instance """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
