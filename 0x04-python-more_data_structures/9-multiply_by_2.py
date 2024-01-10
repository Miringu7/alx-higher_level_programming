#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with
         all values multiplied by 2"""
    new_dict = {value: a_dictionary[value] * 2 for value in a_dictionary}
    return new_dict
