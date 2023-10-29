'''
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to

the adjacent integers and a "valley" is an element which is less than or equal to the adjacent inte-
gers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array
'''

of integers, sort the array into an alternating sequence of peaks and valleys.
EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}
def peaks_and_valleys(array):
  if len(array) < 3:
    return
  for ix in xrange(len(array) - 1):
    # If this is a peak:
    if ix % 2:
      if array[ix] < array[ix + 1]:
        array[ix], array[ix + 1] = array[ix + 1], array[ix]
    # Otherwise, if this is a valley:
    else:
      if array[ix] > array[ix + 1]:
        array[ix], array[ix + 1] = array[ix + 1], array[ix]


import unittest

class Test(unittest.TestCase):
  def test_peaks_and_valleys(self):
    a = [12, 6, 3, 1, 0, 14, 13, 20, 22, 10]
    peaks_and_valleys(a)
    self.assertEqual(a, [6, 12, 1, 3, 0, 14, 13, 22, 10, 20])
    b = [34, 55, 60, 65, 70, 75, 85, 10, 5, 16]
    peaks_and_valleys(b)
    self.assertEqual(b, [34, 60, 55, 70, 65, 85, 10, 75, 5, 16])

if __name__ == "__main__":
  unittest.main()
