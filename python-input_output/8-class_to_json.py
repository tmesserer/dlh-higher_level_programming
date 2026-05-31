#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""


def class_to_json(obj):
    return obj.__dict__
