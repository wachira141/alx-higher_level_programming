#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length < 1:
        return None
    big = my_list[0]
    for i in my_list:
        if i > big:
            big = i
    return big
