#!/usr/bin/python3
digit_collection = ""
def print_last_digit(number):
    global digit_collection
    digit_collection += str(number % 10)
    print(digit_collection)

print_last_digit(9)