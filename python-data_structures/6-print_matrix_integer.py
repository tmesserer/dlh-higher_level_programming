#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        integer_matrix = ""
        for part in matrix:
            for i, number in enumerate(part):
                if i != len(part)-1:
                    integer_matrix += "{:d} ".format(number)
                else:
                    integer_matrix += "{:d}\n".format(number)
        return (integer_matrix)
    else:
        return (matrix)
# print(print_matrix_integer([[1,2,3], [4,5,6], [7,8,9]]))
