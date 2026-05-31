#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""


def save_to_json_file(my_obj, filename):
    """
    Transfrom json string to python object.

    Args:
        my_obj: test to convert
    """
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
