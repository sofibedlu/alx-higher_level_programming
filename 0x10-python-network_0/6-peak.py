#!/usr/bin/python3
"""define a method find_peak """


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (high + low) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
