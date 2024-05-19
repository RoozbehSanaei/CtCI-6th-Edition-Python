'''
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to

the adjacent integers and a "valley" is an element which is less than or equal to the adjacent inte-
gers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array


of integers, sort the array into an alternating sequence of peaks and valleys.
EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}
'''

'''
Objective of Peaks and Valleys:
    The goal is to arrange the array elements so that every second element (starting from the second element) is a peak. This means it should be higher than both its immediate neighbors.

First Swap - Ensuring Higher than Previous Element:
    The first swap in the loop compares the current element with its previous neighbor. If the previous neighbor is higher, they are swapped.
    This swap ensures that the current element is not smaller than its previous element. However, this swap alone doesn't guarantee that the current element is also higher than the next element.

Second Swap - Ensuring Higher than Next Element:
    After the first swap, the current element might still be smaller than its next neighbor.
    The second swap checks and ensures that the current element is also higher than the next element, thus truly making it a peak.

Ensuring a Peak at Each Selected Index:
    By performing both swaps, the algorithm ensures that each selected element (at every odd index) is indeed a peak. It's not enough to just be higher than the previous element; being higher than both neighbors is necessary to form a peak.

Dealing with Array Boundaries:
    The check "If there is an element after the current one" is crucial to avoid index out-of-bound errors. It ensures that the algorithm only tries to swap with a next neighbor if such a neighbor exists.

'''

def peaks_and_valleys(array):
    if len(array) < 3:
        return array

    for ix in range(1, len(array), 2):
        if ix - 1 >= 0 and array[ix] < array[ix - 1]:
            array[ix], array[ix - 1] = array[ix - 1], array[ix]
        
        if ix + 1 < len(array) and array[ix] < array[ix + 1]:
            array[ix], array[ix + 1] = array[ix + 1], array[ix]

    return array


import unittest

class Test(unittest.TestCase):
  def test_peaks_and_valleys(self):
    c = [3, 2, 4]
    peaks_and_valleys(c)

    self.assertEqual(c, [2,4,3])
    a = [12, 6, 3, 1, 0, 14, 13, 20, 22, 10]
    peaks_and_valleys(a)
    self.assertEqual(a, [6, 12, 1, 3, 0, 14, 13, 22, 10, 20])
    b = [34, 55, 60, 65, 70, 75, 85, 10, 5, 16]
    peaks_and_valleys(b)
    self.assertEqual(b, [34, 60, 55, 70, 65, 85, 10, 75, 5, 16])



if __name__ == "__main__":
  unittest.main()