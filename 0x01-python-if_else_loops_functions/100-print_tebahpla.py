#!/usr/bin/python3
x = 0
for i in range(90, 64, -1):
    if x == 32:
        x = 0
    else:
        x = 32
    print('{:c}'.format(i + x), end='')
