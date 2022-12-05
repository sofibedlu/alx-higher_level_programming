#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list_c = my_list.copy()
    for i in range(len(my_list_c)):
        if my_list_c[i] % 2 == 0:
            my_list_c[i] = True
        else:
            my_list_c[i] = False
    return my_list_c
