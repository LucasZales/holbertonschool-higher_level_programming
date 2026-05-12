#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char != 'C' or char != 'c':
            return my_string
