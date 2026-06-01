#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""


class Student:
    """This creates the student class"""

    def __init__(self, first_name, last_name, age):
        """Initiation
        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns all values of instance in dict representation form"""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_dict[attr] = getattr(self, attr)
        return my_dict
