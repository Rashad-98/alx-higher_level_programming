#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = list(map(lambda x: x*2, a_dictionary.values()))
    new_dictionary = {}
    i = 0
    for key in a_dictionary:
        new_dictionary[key] = values[i]
        i = i + 1

    return new_dictionary
