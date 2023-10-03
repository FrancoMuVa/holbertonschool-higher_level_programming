#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Empty Class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of Rectangle

            Args:
                width (int, optional): The width of Rectangle.
                height (int, optional): The height of Rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    print_symbol = "#"

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

    def area(self):
        """ Returns the area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of Rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ Returns a string of the Rectangle to print """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string

        for _ in range(self.__height):
            string += str(self.print_symbol) * self.__width + "\n"

        return string.strip()

    def __repr__(self):
        """ Returns a string representation of the Rectangle """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Print a farewell message when deleting an objet """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2

    @classmethod
    def square(cls, size=0):
        """  Returns a new Rectangle instance """
        return cls(size, size)
