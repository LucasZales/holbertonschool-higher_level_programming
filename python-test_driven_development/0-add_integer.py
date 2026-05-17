#!/usr/bin/python3
"""Module that contains a function to add two integers."""

def add_integer(a, b=98):
    """
    Returns:
        The integer addition of a and b.
    """
    
    if type(a) not in (int, float):
        return "a must be an integer"
    elif type(b) not in (int, float):
        return "b must be an integer"
    return int(a) + int(b)