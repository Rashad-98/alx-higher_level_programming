#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    maximum = float('-inf')
    for i in my_list:
        if i > maximum:
            maximum = i

    return maximum
