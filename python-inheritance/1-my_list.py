#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """A subclass that includes a method to print the list sorted in
    ascending order.
     Example:
        >>> my_list = MyList([3, 1, 4, 2])
        >>> my_list.print_sorted()
        [1, 2, 3, 4]
        >>> print(my_list)
        [3, 1, 4, 2] """
    
    def print_sorted(self):
        """Prints the list in ascending sorted order.
        Example:
            >>> my_list = MyList([5, 2, 9])
            >>> my_list.print_sorted()
            [2, 5, 9] """
        print(sorted(self))
