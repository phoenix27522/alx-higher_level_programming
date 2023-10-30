#!/usr/bin/python3
""" it addes int and floats """


def add_integer(a, b=98):
    """ Adds two numbers, either integers or floats.
    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added. Default is 98.
    Returns:
        int or float: The sum of the two numbers.
    """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
