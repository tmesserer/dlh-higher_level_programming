#!/usr/bin/python3
from sys import argv
numbers = 0
if __name__ == "__main__":
    for number in argv[1:]:
        numbers += int(number)
    print(numbers)
