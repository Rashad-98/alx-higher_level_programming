#!/usr/bin/python3
import hidden_4
if __name__ != '__main__':
    exit()
names = dir(hidden_4)
for name in names:
    if name[0] == '_':
        continue
    print(name)
