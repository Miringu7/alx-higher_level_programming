#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys."""
    sort_a = sorted(a_dictionary)
    for i in sort_a:
        print("{}: {}".format(i, a_dictionary[i], end = "\n"))
