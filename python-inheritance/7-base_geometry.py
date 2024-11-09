#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods for area calculation and
integer validation.
"""


class BaseGeometry:
    """
    A class representing the concept of geometry."""
    def area(self):
        """
        Public instance method that raises an exception indicating
        that the method is not yet implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"<name> must be an integer")
        if value <= 0:
            raise ValueError(f"<name> must be greater than 0")
