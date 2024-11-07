#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square
with a private instance attribute for its size.
"""


class Square:
    """
    This class represents a square with a private attribute `size`.
    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the `Square` class.
        Also, raise exceptions in certain cases.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A public method that returns the current square area"""
        return(self.__size * self.__size)
