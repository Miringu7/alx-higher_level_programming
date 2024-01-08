#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    if matrix:
        for row in range(len(matrix)):
            for element in range(len(matrix[row])):
                if element != len(matrix[row]) - 1:
                    end_space = ' '
                else:
                    end_space = ''
                print("{:d}".format(matrix[row][element]), end=end_space)
            print()
    else:
        print()
