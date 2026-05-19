#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """an empy class with nothing"""

    def __init__(self, size=0):
        self.__size = int(size)
        if size != int(size):
            raise TypeError("size must be and integer")
        if size < 0:
            raise ValueError("size must be >= 0")
