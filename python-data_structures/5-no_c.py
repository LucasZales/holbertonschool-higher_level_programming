#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for char in my_string:
        if char != 'C' or char != 'c':
            new_list += char
    return new_list
