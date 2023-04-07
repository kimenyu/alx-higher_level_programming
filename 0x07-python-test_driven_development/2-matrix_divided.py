#!/usr/python3
"""matrix divider module"""
def matrix_divided(matrix, div):
     """divides a matrix all elements by divider
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