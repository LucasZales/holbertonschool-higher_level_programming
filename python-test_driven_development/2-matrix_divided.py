#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Returns a new matrix with all values divided by div."""

    # validation of div
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # validation
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])

    for row in matrix:

        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for num in row:
            if type(num) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )

    # matrix
    new_matrix = []

    for row in matrix:
        new_row = []

        for num in row:
            new_row.append(round(num / div, 2))

        new_matrix.append(new_row)

    return new_matrix
