#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 <= idx <= len(my_list)-1:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
    else:
        print("None")
