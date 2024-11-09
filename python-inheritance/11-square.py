#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special type of rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with a given size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
