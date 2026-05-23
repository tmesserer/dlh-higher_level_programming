#!/usr/bin/python3
"""Module that defines a class called Square"""


class Square:
    """
    This is my class Square.
    It is a geometrical figure with four sides of equal length that is closed.
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): Gives the size of the square, aka how big it is.
            Defaults to 0.
        """

        self.__size = size

    @property
    def size(self):
        """This is the getter method of size and creates the property"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter method for size.
        Raises:
            TypeError: size has to be an integer
            ValueError: size has to be equal or larger than 0 to be valid
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Args:
            no argument used except self

        Method:
            returns the area of the square, which is size
            squared (multiplied by itself)
        """
        return self.__size * self.__size
