#!/usr/bin/python3

""" a class representing a square """


class Square:
    """
    square - defins its size
    args :
         size: size of the square
    """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
