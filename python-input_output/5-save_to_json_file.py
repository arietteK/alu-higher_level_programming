#!/usr/bin/python3
"""defining the save_to_json_file function with two parameters"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using the JSON representation."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
