#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    key = list(a_dictionary)[0]
    max_s = a_dictionary[key]
    for i in a_dictionary:
        if isinstance(a_dictionary[i], int):
            if max_s < a_dictionary[i]:
                max_s = a_dictionary[i]
    return max_s
