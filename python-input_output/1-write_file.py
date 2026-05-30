#!/usr/bin/python3
"""
This module is used for the project input/output.
Currently there is a function that reads a file.
"""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file, creating it if it doesn't exist.
    Args:
        filename: path to file to write
        text: text to write in file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
