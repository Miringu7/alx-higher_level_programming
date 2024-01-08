#!/usr/bin/env python3

def no_c(my_string):
    """function that removes all characters c and C from a string."""
    new_string = ""
    for elements in my_string:
        if elements != 'c' and elements != 'C':
            new_string += elements
    return new_string
