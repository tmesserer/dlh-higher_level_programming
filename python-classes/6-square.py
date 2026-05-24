#!/usr/bin/python3
"""Module that defines a class called Square"""


class Square:
    """
    This is my class Square.
    It is a geometrical figure with four sides of equal length that is closed.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): Gives the size of the square, aka how big it is.
            Defaults to 0.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This is the getter method of position and creates the property"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is the setter method for position.
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Args:
            no argument used except self

        Method:
            returns the area of the square, which is size
            squared (multiplied by itself)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Method that prints in stdout the square with the character #.
        The position tuple (x, y) - x creates "_" before the "#";
            y creates an empty row before
        """
        if self.size == 0:
            print("")
            return

        for h in range(0, self.position[1]):
            print("")
        for i in range(0, self.size):
            print(" " * self.position[0] + "#" * self.size)
