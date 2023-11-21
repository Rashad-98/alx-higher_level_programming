#!/usr/bin/python3
"""module with only one class"""


class Square:
    """class that represents a square
    the class validates the size upon instantiation
    of an instance
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return size * size
