#!/usr/bin/python3
""" Function that prints a square of # """


def print_square(size):
    """ prints a square shaped of #
    Args:
        size(int): the hight and length of the square
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than or equal to 0.

    Returns: square shaped containing of #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
