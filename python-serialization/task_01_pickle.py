#!/usr/bin/env python3
"""Modul used for serialization and de-serialization"""
import pickle


class CustomObject:
    """
    This creates the CustomObject class.
    """

    def __init__(self, name, age, is_student):
        """
        Args:
            name:
            age:
            is_student:
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displays all attributes in dictionary format"""
        for key, value in self.__dict__.items():
            print("{}: {}".format(key.replace("_", " ").title(), value))

    def serialize(self, filename):
        """serializes its attributes in the attribute filename"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """This class method will take a filename as its parameter.
        Using the pickle module, it will load and return an instance of
        the CustomObject from the provided filename.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
