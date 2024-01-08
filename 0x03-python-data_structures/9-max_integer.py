#!/usr/bin/python3

def max_integer(my_list=[]):
    """function that finds the biggest integer of a list."""
    if my_list:
        max = 0
        for value in my_list:
            if value > max:
                max = value
        return max
    else:
        return None
