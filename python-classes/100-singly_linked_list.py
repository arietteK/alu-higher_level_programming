#!/usr/bin/python3
"""A linked list oop module"""


class Node:
    """A class node that defines a node of a singly linked list
    data represents the information and
    next_node represents the next container in the list that houses the data """

    def __init__(self, data, next_node=None):
        """The instantiation of method"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """the getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data with type checking."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for the next_node with type checking."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""
    def __init__(self):
        """The initialization"""
        self.__head = None

    def sorted_insert(self, value):
         """Insert a new Node into the correct sorted position in the list (increasing order)."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and 
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """A method that prints the list"""
        result = []
        tmp = self.__head
        while tmp:
            result.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(result))
