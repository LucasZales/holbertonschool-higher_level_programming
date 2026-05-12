#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            new_list += char
    return new_list
