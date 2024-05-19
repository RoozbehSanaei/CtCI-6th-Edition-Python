# Bisect the squares.

import unittest
import random
from dataclasses import dataclass

@dataclass
class Point():
    x : float
    y : float

@dataclass
class Square():
    center: Point
    side_length: float
    rotation: float

def bisect_squares(sq1: Square, sq2: Square):
    x_diff = sq2.center.x - sq1.center.x
    y_diff = sq2.center.y - sq1.center.y
    if (y_diff==0): return lambda x:sq1.center.y
    if (x_diff==0): return None
    slope = y_diff/x_diff
    intercept = sq1.center.y - slope*sq1.center.x
    return lambda x: slope*x + intercept

class TestBisectSquares(unittest.TestCase):
    def test_fixed_squares(self):
        sq1 = Square(Point(2, 4.5), 2, 15)
        sq2 = Square(Point(7, 4.5), 3, 45)
        line = bisect_squares(sq1, sq2)
        self.assertEqual(line(0), 4.5)
        self.assertEqual(line(11), 4.5)
    
    def test_random_squares(self):
        for _ in range(10):
            center1 = Point(random.uniform(-10, 10), random.uniform(-10, 10))
            center2 = Point(random.uniform(-10, 10), random.uniform(-10, 10))
            square1 = Square(center1, random.uniform(1, 9), random.uniform(0, 90))
            square2 = Square(center2, random.uniform(1, 9), random.uniform(0, 90))
            line = bisect_squares(square1, square2)
            with self.subTest(center1=center1, center2=center2):
                self.assertAlmostEqual(line(center1.x), center1.y, places=7)
                self.assertAlmostEqual(line(center2.x), center2.y, places=7)
                mid_x = (center1.x + center2.x) / 2
                mid_y = (center1.y + center2.y) / 2
                self.assertAlmostEqual(line(mid_x), mid_y, places=7)

    def test_vertical_line(self):
        center1 = Point(5, 5)
        center2 = Point(5, 10)
        square1 = Square(center1, 2, 0)
        square2 = Square(center2, 2, 0)
        line = bisect_squares(square1, square2)
        self.assertIsNone(line)

    def test_same_center(self):
        center = Point(5, 5)
        square1 = Square(center, 2, 0)
        square2 = Square(center, 2, 0)
        line = bisect_squares(square1, square2)
        self.assertEqual(line(0), 5)
        self.assertEqual(line(10), 5)

if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
  unittest.main()

