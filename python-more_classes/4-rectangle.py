#!/usr/bin/python3
"""This module defines a class that represents a rectangle with properties
for width and height, and methods to calculate area, perimeter,
printing with `#`, and recreating new instances using `eval()`."""


class Rectangle:
    """The rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the  class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation.
        Args:value (int): The new width value.
        Raises: TypeError and ValueError"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation.
        Args: value (int): The new height value.
        Raises TypeError and ValueError"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using
        the `#` character."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle that can be used
        to recreate a new instance using `eval()`."""
        rect_rep = "Rectangle(" + str(self.__width)
        rect_rep += ", " + str(self.__height) + ")"
        return rect_rep
