# Bisect the squares.

import unittest
import random

def bisect_squares(square1, square2):
  center1, center2 = square1.center, square2.center
  xdiff = center2.x - center1.x
  ydiff = center2.y - center1.y
  if xdiff == 0:
    if ydiff == 0:
      return lambda x: center1.y
    else:
      # Vertical line.
      return None
  slope = float(ydiff) / xdiff
  intercept = center1.y - center1.x * slope
  return lambda x: slope * x + intercept

class Square(object):
  def __init__(self, center, side_length, rotation):
    self.center, self.side_length, self.rotation = center, side_length, rotation

class Point(object):
  def __init__(self, x, y):
    self.x, self.y = x, y


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

