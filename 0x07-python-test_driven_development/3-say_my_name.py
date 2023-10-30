#!/usr/bin/python3
""" Function that print a full name """


def say_my_name(first_name, last_name=""):
    """ Prints a full name
    Args:
        first_name(string): first name
        last_name(string): second name

    Returns: string a full name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
