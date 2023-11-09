#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_to_int_store = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    integers = []
    sum = 0

    for i in roman_string:
        if i in roman_to_int_store:
            integers.append(roman_to_int_store[i])

    for i in range(-1, (-1 * len(integers)) - 1, -1):
        if i == -1:
            sum = integers[i]
            continue
        if integers[i] < integers[i + 1]:
            sum -= integers[i]
        else:
            sum += integers[i]

    return sum
