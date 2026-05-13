#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxm = my_list[0] 
    for number in my_list:
        if number > maxm:
            maxm = number
    return maxm
