# O(NxN)
import unittest
from copy import deepcopy

'''
The rotate_matrix function rotates a given matrix 90 degrees clockwise. It does this by moving elements in layers, starting from the outermost layer and moving inward. For each layer, it performs a four-way swap:

    Saves the top elements.
    Moves the left elements to the top.
    Moves the bottom elements to the left.
    Moves the right elements to the bottom.
    Places the saved top elements to the right.

This process is repeated for each layer of the matrix until all layers have been rotated. The function then returns the rotated matrix.
'''


def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # top -> right
            matrix[i][-layer - 1] = top
    return matrix

'''
The rotate_matrix_double_swap function rotates a given matrix by 90 degrees clockwise. It does this in two main steps:

Transpose the matrix: This is done by swapping elements across the diagonal. For each pair of elements matrix[i][j] and matrix[j][i] where i < j, the function swaps their positions.

Swap columns: For each row, the function swaps elements from the start and end of the row, moving towards the center. This effectively reverses each row.

These two steps combined result in a 90-degree clockwise rotation of the matrix. The function returns the rotated matrix.


'''


def rotate_matrix_double_swap(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp
    return matrix


def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # empty list of 0s
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result


def rotate_matrix_pythonic_alternate(matrix):
    """rotates a matrix 90 degrees clockwise"""
    return [list(reversed(row)) for row in zip(*matrix)]


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate_matrix_pythonic,
        rotate_matrix,
        rotate_matrix_pythonic_alternate,
        rotate_matrix_double_swap,
    ]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
