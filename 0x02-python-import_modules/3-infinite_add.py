#!/usr/bin/python3
if __name__ != "__main__":
    exit()
from sys import argv
if len(argv) == 1:
    print(0)
    exit()

sum = 0
for i in argv[1:]:
    sum += int(i)

print(sum)
