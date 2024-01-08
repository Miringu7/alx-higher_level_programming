#!/usr/bin/python3

def multiple_returns(sentence):
    """function that returns a tuple with the length
        of a string and its first character."""
    if sentence:
        new_tuple = (len(sentence), sentence[0])
        return new_tuple
    else:
        new_tuple = (0, None)
        return new_tuple
