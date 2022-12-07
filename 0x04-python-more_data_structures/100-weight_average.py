#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    sum_s = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        result += (i[0] * i[1])
        sum_s += i[1]
    return result / sum_s
