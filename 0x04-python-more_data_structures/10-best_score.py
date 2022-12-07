#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_s = a_dictionary[next(iter(a_dictionary))]
    for i in a_dictionary:
        if max_s < a_dictionary[i]:
            max_s = a_dictionary[i]
    return max_s
