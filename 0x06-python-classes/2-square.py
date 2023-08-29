#!/usr/bin/python3
"""Create class Square."""


class Square:
    """form square."""

    def __init__(self, size=0):
        """Initialize Square.

        Args:
            size (int): The size new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
