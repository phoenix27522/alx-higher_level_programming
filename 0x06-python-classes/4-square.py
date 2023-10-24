#!/usr/bin/python3

""" a class representing a square """


class Square:
    """
    square - defins its size
    args :
         size: size of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ gets the size of the sequare """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size and handdel the exception """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
