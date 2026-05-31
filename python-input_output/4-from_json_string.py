#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""


def from_json_string(my_str):
    """
    Transfrom json string to python object.

    Args:
        my_obj: test to convert
    """
    import json
    return json.loads(my_str)
