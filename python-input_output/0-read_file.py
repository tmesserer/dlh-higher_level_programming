#!/usr/bin/python3
"""
This module is used for the project input/output.
Currently there is a function that reads a file.
"""


def read_file(filename=""):
    """This function opens a text file (UTF8),
    then prints its content one line after another"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
