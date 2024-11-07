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
    def __init__(self, size):
        """
        Initializes a new instance of the `Square` class.
        """
        self.__size = size
