#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """an empy class with nothing"""

    def __init__(self, size=0):
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
