#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if b == a:
            continue
        elif (10 * a + b) > (10 * b + a):
            continue
        else:
            print("{}{}".format(a, b), end="\n" if a == 8 and b == 9 else ", ")
