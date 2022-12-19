#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            n += 1
        print()
    except IndexError:
        print()
    return n
