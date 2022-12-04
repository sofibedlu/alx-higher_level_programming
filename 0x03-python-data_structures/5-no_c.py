#!/usr/bin/python3
def no_c(my_string):
    lists = []
    my_str = ""
    n = 0
    for i in range(len(my_string)):
        lists.append(my_string[i])
    for i in lists:
        if lists[n] == 'c' or lists[n] == 'C':
            del lists[n]
        n += 1
    for i in lists:
        my_str += i
    return (my_str)
