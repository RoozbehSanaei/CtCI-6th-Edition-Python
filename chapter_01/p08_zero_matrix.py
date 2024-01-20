# O(MxN)
import unittest
from copy import deepcopy

'''
The zero_matrix function sets entire rows and columns to zero in a given matrix if any element in those rows or columns is zero. It operates in two main steps:

    Identifying Rows and Columns with Zeros:
        It iterates through each element in the matrix.
        If an element is zero, it adds its row and column indices to the rows and cols sets, respectively.

    Setting Rows and Columns to Zero:
        It iterates again through each element in the matrix.
        If the current element's row or column index is in the rows or cols sets, it sets that element to zero.

The function then returns the modified matrix, where all rows and columns that contained at least one zero element have been entirely set to zero.
'''


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix

'''
The zero_matrix_pythonic function sets entire rows and columns to zero in a given matrix if any element in those rows or columns is zero. This Pythonic approach involves:

    Replacing all zero elements in the matrix with "X". Using "X" instead of zeros avoids  changing rows or columns that didn't originally contain zeros.
    Identifying rows containing "X" and setting all elements in these rows to zero, while recording the column indices of "X".
    Setting all elements in the identified columns to zero.
    Returning the modified matrix with specified rows and columns set to zero.
'''


def zero_matrix_pythonic(matrix):
    matrix = [["X" if x == 0 else x for x in row] for row in matrix]
    indices = []
    for idx, row in enumerate(matrix):
        if "X" in row:
            indices = indices + [i for i, j in enumerate(row) if j == "X"]
            matrix[idx] = [0] * len(matrix[0])
    matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [zero_matrix, zero_matrix_pythonic]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
