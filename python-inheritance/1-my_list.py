#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """A subclass of list that includes a method to print the list sorted in
    ascending order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
