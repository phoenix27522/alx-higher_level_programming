#!/usr/bin/python3
""" defines a class Rectangle that inherites from BaseGeometry. """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represent rectangle using BaseGeometry """

    def __init__(self, width, height):
        """ initalize a new Rectangle """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
