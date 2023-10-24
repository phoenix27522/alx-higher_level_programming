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
        """ gets the value of the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of the size """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ finds the area of square"""

        return self.__size ** 2

    def my_print(self):
        """ Prints the area in the form # """
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()


        if self.__size == 0:
            print("")
