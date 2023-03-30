#!/usr/bin/python3
"""define a method find_peak """

def find_peak(list_of_integers):
    """find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    return sorted(list_of_integers)[-1]
