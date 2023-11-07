#!/usr/bin/python3
def no_c(my_string):
    index = -2
    while True:
        index = my_string.find('c')
        if index == -1:
            break
        my_string = my_string[:index] + my_string[index+1:]

    index = -2
    while True:
        index = my_string.find('C')
        if index == -1:
            break
        my_string = my_string[:index] + my_string[index+1:]

    return my_string
