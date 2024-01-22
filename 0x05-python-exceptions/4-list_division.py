#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists."""
    new_list = []
    zero = 0
    for i in range(0, list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            new_list.append(zero)
            continue
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(zero)
            continue
        except IndexError:
            print("out of range")
            new_list.append(zero)
            continue
    return new_list
