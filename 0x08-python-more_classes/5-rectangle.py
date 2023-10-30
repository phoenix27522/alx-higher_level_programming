#!/usr/bin/python3
""" class with setter and getters """


class Rectangle:
    """ class that defines rectangle
    Args:
        width(int): width of the rectangle
        height(int): hieght of the rectangle
    Raises:
        TypeError: if the width and hieght are not int
        ValueError: if width and height < 0
    """

    def __init__(self, width=0, height=0):
        """ initiates the variable of the rectangle """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter of the variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of the variable width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ getter of the variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of the variable height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the parameter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Return the printable representation of the Rectangle
        consisting of the #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += "#"
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__ (self):
        """ prints somthing when instance is deleted """
        print("Bye rectangle...")
