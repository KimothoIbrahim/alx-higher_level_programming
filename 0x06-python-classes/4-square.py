#!/usr/bin/python3
"""Create class Square."""


class Square:
    """SEt up a square."""

    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): The size square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)
