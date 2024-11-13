#!/usr/bin/python3
"""defining a read_file function"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
