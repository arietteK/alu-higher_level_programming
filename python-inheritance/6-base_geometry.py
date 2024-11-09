#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a method that raises
an exception."""


class BaseGeometry:
    """
    A class representing the concept of geometry."""
    def area(self):
        """
        Public instance method that raises an exception indicating
        that the method is not yet implemented."""

        raise Exception("area() is not implemented")
