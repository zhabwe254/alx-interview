#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): The input n x n 2D matrix.

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
