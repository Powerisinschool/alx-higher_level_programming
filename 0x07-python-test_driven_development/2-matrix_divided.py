#!/usr/bin/python3
""" Matrix division function """


def matrix_divided(matrix, div):
    """
    This function divides a matrix
    Return - matrix / div
    """
    if(not isinstance(matrix, list) or matrix == [] or
       not all(isinstance(row, list) for row in matrix) or
       not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists) \
    of integers/floats')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[ round(x / div, 2) for x in row] for row in matrix]
