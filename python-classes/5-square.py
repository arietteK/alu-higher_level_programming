#!/usr/bin/python3
"""This module defines a class `Square` that represents a square"""


class Square:
    """ This class represents a square with a private attribute `size`."""

    def __init__(self, size=0):
        """Initializes a new instance of the `Square` class."""

        self.__size = size

        """Getter for the private attribute size"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A public method that returns the current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """print repetition of square with # character"""
        if self.__size == 0:
            print()
        for item i in range(self.__size):
            [print("#", end='') for j in range(self.__size)]
            print()
