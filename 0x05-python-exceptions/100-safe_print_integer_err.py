#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """function that prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    return True
