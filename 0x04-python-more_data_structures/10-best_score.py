#!/usr/bin/python3

def best_score(a_dictionary):
    """function that returns a key with the biggest integer value."""
    if a_dictionary:
        max = 0
        for value in a_dictionary:
            if a_dictionary[value] > max:
                max = a_dictionary[value]
                max_value = value
        return max_value
    return None
