#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for part in matrix:
        for i, number in enumerate(part):
            if i != len(part)-1:
                print("{:d}".format(number), end=" ")
            else:
                print("{:d}".format(number), end="")
        print()
