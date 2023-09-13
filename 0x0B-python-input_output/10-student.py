#!/usr/bin/python3
"""Class Student."""


class Student:
    """Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary representation of Student.

        Args:
            attrs (list): Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
