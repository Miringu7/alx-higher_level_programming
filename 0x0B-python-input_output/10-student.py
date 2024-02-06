#!/usr/bin/python3
"""Defines a student class"""


class Student():
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """student constructor

        Args:
            first_name: student last name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs: attributes
        Return:
            dictionary representation of a Student instance
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}

        return self.__dict__
