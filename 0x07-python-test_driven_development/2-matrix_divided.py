#!/usr/bin/python3


def matrix_divided(matrix, div):
    ''' Check if the input matrix is valid
    '''


    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    '''Check if all rows have the same size'''

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    '''Check if div is a number
    '''

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    '''Check if div is not zero
    '''

    if div == 0:
        raise ZeroDivisionError("division by zero")
    ''''Divide each element of the matrix by div and round to 2 decimal places
    '''
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
