#!/usr/bin/python3
"""returns True if the object is an instance of the specified class"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class or inherited class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
