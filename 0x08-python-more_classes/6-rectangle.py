#!/usr/bin/python3
"""define class 'Rectangle'"""


class Rectangle:
    """Rep a rectangle"""

    def __init__(self, width=0, height=0):

        """initialize new instance of rectangle

        Args:
            width (int): width of triangle
            height (int): height of triangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height of rect"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ret area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """return rect perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """Return rep of rectangle using #"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []

        for x in range(self.__height):
            [rectangle.append('#') for p in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """ return string representation"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """print a message for deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
