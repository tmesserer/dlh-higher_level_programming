#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""


def to_json_string(my_obj):
    """
    Transfrom text to json string.

    Args:
        my_obj: test to convert
    """
    import json
    return json.dumps(my_obj)
