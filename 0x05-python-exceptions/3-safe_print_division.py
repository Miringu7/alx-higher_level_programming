#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the result."""
    div_result = None
    try:
        div_result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        return None
    finally:
        print("Inside result: ", "{:.1f}".format(div_result) if div_result
              is not None else "None")
    return div_result
