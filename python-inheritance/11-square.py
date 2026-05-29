#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
