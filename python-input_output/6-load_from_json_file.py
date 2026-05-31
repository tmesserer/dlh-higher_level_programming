#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""


def load_from_json_file(filename):
    """
    Transfrom json string to python object.

    Args:
        my_obj: test to convert
    """
    import json
    with open(filename, "r") as f:
        return json.load(f)
