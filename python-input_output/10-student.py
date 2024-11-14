#!/usr/bin/python3
"""Contains the class Student"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is not None and isinstance(attrs, list):
            return {key: value 
                    for key, value in self.__dict__.items() if key in attrs
                    }

        return self.__dict__
