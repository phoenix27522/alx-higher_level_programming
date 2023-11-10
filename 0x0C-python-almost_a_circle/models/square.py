#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square, which is a special case of a Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes based on no-keyword and keyword arguments."""
        attr_names = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
