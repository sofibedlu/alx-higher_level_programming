#!/usr/bin/python3
def max_integer(my_list=[]):
    maxm = 0
    if len(my_list) == 0:
        return None
    if isinstance(my_list, list):
        for i in my_list:
            if i >= maxm:
                maxm = i
    return maxm
