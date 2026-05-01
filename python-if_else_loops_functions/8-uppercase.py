#!/usr/bin/python3
def uppercase(str):
    all_uppercase = ""
    for a in str:
        if ord(a) in range(97, 123):
            all_uppercase += chr((ord(a) - 32))
        else:
            all_uppercase += chr(ord(a))
    print(all_uppercase.format())
