#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_i = min(my_list)
    for i in my_list:
        if i > max_i:
            max_i = i

    return max_i
