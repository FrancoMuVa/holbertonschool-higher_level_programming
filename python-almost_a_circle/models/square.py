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

    def update(self, *args, **kwargs):
        """ Update argument to each attribute """
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def __str__(self):
        """ Returns a string reprecentation of Square instance """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dict
