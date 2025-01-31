#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
