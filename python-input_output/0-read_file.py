#!/usr/bin/python3
"""
I/O utilities for reading and displaying project data files.
Focuses currently on UTF8 text files.
"""


def read_file(filename=""):
    """Open a text file (UTF8),
    then printsthe contents to stdout."""
    with open(filename) as f:
        for line in f:
            print(line, end="")
