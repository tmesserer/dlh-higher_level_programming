#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    new_list = []
    previous_variable = "ZZZ"
    if not roman_string:
        return result
    else:
        dict = {"ZZZ": 9999, "I": 1, "V": 5, "X": 10, \n
                "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in roman_string:
            if dict.get(i) <= dict.get(previous_variable):
                new_list.append(dict.get(i))
                previous_variable = i
            else:
                new_list[-1] = -new_list[-1]
                new_list.append(dict.get(i))
                previous_variable = i
        for x in range(0, len(new_list)):
            result += new_list[x]
        print(new_list)
        return result
