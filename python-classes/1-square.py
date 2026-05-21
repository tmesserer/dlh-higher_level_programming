#!/usr/bin/python3
"""Module that defines a class called Square"""


class Square:
    """
    This is my class Square.
    It is initiated with a private instance attribute '__size' 
    """
    def __init__(self, size):
        """
        Method to initiate the instance and give it a private size
        """
        self.__size = size
