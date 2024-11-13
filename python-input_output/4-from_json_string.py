#!/usr/bin/python3
"""defining the from_json_string with one parameter"""

import json


def from_json_string(my_str):
    """Returns a JSON string."""
    return json.loads(my_str)
