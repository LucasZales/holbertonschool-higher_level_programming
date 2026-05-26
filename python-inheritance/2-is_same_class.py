#!/usr/bin/python3
"""function that checks if the object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """return True is obj is exactly an instance of a_class"""
    return type(obj) is a_class
