#!/usr/bin/python3
"""
This module provides a function
that prints pascal's triangle.
Up to the n-th level.
"""


def pascal_triangle(n):
    """
    prints out pascal's triangle.
    Arguments:
        n: defines the level to which the triangle is built.
    """
    if n <= 0:
        return []
    last_row = [1]
    current_row = []
    for i in range(0, n):
        if i == 0:
            print("[1]")
            continue
        elif last_row == [] or last_row == [1]:
            current_row.append(1)
        else:
            current_row.append(last_row[0])
        for j in range(0, len(last_row)):
            if j+1 < len(last_row):
                current_row.append(last_row[j] + last_row[j+1])
        current_row.append(1)
        print(current_row)
        if len(last_row) > 0:
            last_row = current_row
        current_row = []
