#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Student representation."""

    def __init__(self, first_name, last_name, age):
        """new Student.

        Args:
            first_name (str): The student's first name..
            last_name (str): Their last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of Student."""
        return self.__dict__
