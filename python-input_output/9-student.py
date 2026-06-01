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

    def to_json(self):
        """returns all values of instance in dict representation form"""
        return self.__dict__
