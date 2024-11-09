#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a specified class or an instance of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False """
    return isinstance(obj, a_class)
