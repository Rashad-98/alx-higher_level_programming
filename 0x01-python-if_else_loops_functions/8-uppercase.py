#!/usr/bin/python3
def uppercase(str):
    str_cpy = ''
    for i in range(len(str)):
        inc = ord(str[i])
        if inc >= 97 and inc <= 122:
            str_cpy += '{:c}'.format(inc - 32)
        else:
            str_cpy += str[i]
    print(str_cpy)
