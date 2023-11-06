#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle (9-rectangle.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
