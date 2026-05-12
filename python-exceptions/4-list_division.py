#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        else:
            new_list.append(my_list_1[i] / my_list_2[i])
        finally:
            return new_list
list_division([10, 8, 4], [5, 4, 2], 3)

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 2]
list_length = 5
new_list = []
for i in range(0, list_length):
    new_list.append(my_l_1[i] / my_l_2[i])
print(new_list)

# Exceptions:
# ZeroDivisionError for div / 0 --> "division by 0"
# TypeError: unsupported operand type(s) for string, dict, etc --> "wrong type"
# IndexError: one list too short or list_length too long --> "out of range"
