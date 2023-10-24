#!/usr/bin/python3

""" a class representing a square """


class Square:
    """
    square - defins its size
    args :
         size: size of the square
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ finds the area of square"""

        return self.__size ** 2
