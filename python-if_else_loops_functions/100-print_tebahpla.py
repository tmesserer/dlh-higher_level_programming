#!/usr/bin/python3
for i in range(122, 64, -1):
    if i % 2 == 0 and i > 96:
        print(chr(i), end="")
    elif i % 2 == 1 and i > 95:
        print(chr(i-32), end="")
    else:
        pass
