#!/usr/bin/python3
import json
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        with open (file_name, 'w') as file:
            json_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def to_json_string(list_dict):
        """Converts a list of dictionaries to a JSON string."""
        return json.dumps(list_dict)

    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)
