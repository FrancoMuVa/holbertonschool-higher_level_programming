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
            Initializes a new isinstance of the Rectangle class.

            Args:
                width:  (int) The width of rectangle.
                height: (int) The height of the rectangle.
                x:      (int, optional) The x coordinate.
                y:      (int, optional) The x coordinate.
                id:     (int, optional) The ID value.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """  Getter for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """  Getter for the x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """  Getter for the y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("{}".format(" " * self.__x + "#" * self.__width))

    def __str__(self):
        """ Returns a string with the reprecentation of the Rectangle """
        x_y = f"{self.__x}/{self.__y}"
        width_height = f"{self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {x_y} - {width_height}"

    def update(self, *args, **kwargs):
        """ Updates argument to each attribute """
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return dict
