#!/usr/bin/python3
"""Class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get representation of the Student

         Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes

        Args:
            json (dict): what to replace attributes with.
        """
        for ke, va in json.items():
            setattr(self, ke, va)
