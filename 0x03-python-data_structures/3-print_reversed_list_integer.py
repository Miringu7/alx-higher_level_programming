#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""
    j = -1
    if my_list:
        for i in range(len(my_list)):
            print("{:d}".format(my_list[j]))
            j -= 1
