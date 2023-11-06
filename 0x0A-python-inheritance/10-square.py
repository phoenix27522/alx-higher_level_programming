#!/usr/bin/python3
""" defines a square from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square that inherits from rectangle """
    def __init__(self, size):
        """ Initialize a new Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
