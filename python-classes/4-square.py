#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """an empy class with nothing"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must >= 0")
        self.__size = value
