#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for digit in range(0, len(my_list)):
        print("{}".format(my_list[digit]))
print_list_integer([1, 2, 3, 4, 5])