import unittest
from typing import List


'''
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
'''


def flood_fill(screen: List[List[int]], i: int, j: int, color: int, new_color: int):
    if (
        i < 0
        or i >= len(screen)
        or j < 0
        or j >= len(screen[0])
        or screen[i][j] != color
    ):
        return
    screen[i][j] = new_color
    flood_fill(screen, i + 1, j, color, new_color)
    flood_fill(screen, i - 1, j, color, new_color)
    flood_fill(screen, i, j + 1, color, new_color)
    flood_fill(screen, i, j - 1, color, new_color)


def paint_fill(
    screen: List[List[int]], r: int, c: int, new_color: int
) -> List[List[int]]:
    if not screen:
        return None

    color = screen[r][c]
    flood_fill(screen, r, c, color, new_color)
    return screen


class Test(unittest.TestCase):
    test_cases = [
        (
            [[1, 2, 5], [2, 2, 4], [2, 8, 6]],
            1,
            1,
            3,
            [[1, 3, 5], [3, 3, 4], [3, 8, 6]],
        )
    ]
    testable_functions = [paint_fill]

    def test_paint_fill(self):
        for f in self.testable_functions:
            for [screen, r, c, new_color, expected] in self.test_cases:
                assert f(screen, r, c, new_color) == expected


if __name__ == "__main__":
    unittest.main()
