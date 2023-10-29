'''
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to

the adjacent integers and a "valley" is an element which is less than or equal to the adjacent inte-
gers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array


of integers, sort the array into an alternating sequence of peaks and valleys.
EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}
'''

def peaks_and_valleys(array):
    # If the array has less than three elements, it's not possible to properly create peaks and valleys.
    # In this case, simply return the original array.
    if len(array) < 3:
        return array
    
    # Iterate through the array starting from index 1 (the second element),
    # and skip every second element. The goal is to create peaks at every odd index.
    for ix in range(1, len(array) - 1, 2):
        
        # Compare the current element (which we want to be a peak) with its previous neighbor.
        # If the previous neighbor is greater, swap them.
        # This operation ensures that array[ix] is not smaller than array[ix - 1].
        if array[ix - 1] > array[ix]:
            array[ix], array[ix - 1] = array[ix - 1], array[ix]
            
        # Now, compare the current element (which we are turning into a peak) with its next neighbor.
        # If the next neighbor is greater, swap them.
        # This operation ensures that array[ix] is not smaller than array[ix + 1].
        if ix + 1 < len(array) and array[ix] < array[ix + 1]:
            array[ix], array[ix + 1] = array[ix + 1], array[ix]
    
    # Return the modified array, which should now have peaks at every odd index.
    return array

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
