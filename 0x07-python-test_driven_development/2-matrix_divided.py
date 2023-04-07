#!/usr/bin/python3

"""
2-matrix_divided
Contains method that divides all elements of a matrix and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""

def matrix_divided(matrix, div):

     """
    Returns new matrix with dividends
    """

    if not isinstance((element,  (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(row) != len(matrix[0] for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
            new_matrix.append(new_row)
            return new_matrix
