#!/usr/bin/python3
"""
This module defines a class `Square` that represents a square
with a private instance attribute for its size.
"""


class Square:
    """ This class represents a square with a private attribute `size`."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the newly created square
        where: size equates the size of the square and given a default value 0
        position is a tuple """
        self.__size = size
        self.position = position

        """Getter for the private attribute size"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Make the value of the set meet a standard"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Private instance attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter def position(self, value): to set it"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A public method that returns the current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """print repetition of square with # character"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
