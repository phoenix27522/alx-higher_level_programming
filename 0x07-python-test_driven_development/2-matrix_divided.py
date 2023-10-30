#!/usr/bin/python3
""" This function divides the matrix """


def matrix_divided(matrix, div):
    """Divides the matrix by int or float

    Args:
        matrix: The matrix to be divided
        div: a number that is going to divide the matrix

    Returns:
           a new matrix: the dividen of each element on the matrix

    """
    if not isinstance(matrix, list)\
            or not all(isinstance(raw, list) for raw in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(n, (int, float)) for row in matrix for n in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for raw in matrix:
        resulted_raw = [round(n/div, 2) for n in raw]
        new_matrix.append(resulted_raw)
    return new_matrix
