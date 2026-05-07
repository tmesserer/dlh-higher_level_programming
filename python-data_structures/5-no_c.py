#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if letter == "c":
            pass
        elif letter == "C":
            pass
        else:
            print("{}".format(letter), end="")
