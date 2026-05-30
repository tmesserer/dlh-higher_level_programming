#!/usr/bin/python3
"""
This module is used for the project input/output.
Currently there is a function that reads a file and appends the text.
"""


def append_write(filename="", text=""):
    """
    Append text to a UTF-8 file, creating it if it doesn't exist.

    Args:
        filename: path to file to write
        text: text to write in file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
