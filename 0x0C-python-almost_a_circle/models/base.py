#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """ parent class for all classes in this project.
        The goal of it is to manage id attribute in
        all your future classes and to avoid duplicating
        the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the id argument """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
