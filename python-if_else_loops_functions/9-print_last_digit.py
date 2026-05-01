#!/usr/bin/python3
def print_last_digit(number):
    digit_collection = (abs(number) % 10)
    print(digit_collection, end="")
    return digit_collection
