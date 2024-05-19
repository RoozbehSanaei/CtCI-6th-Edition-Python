import unittest
# Return the bounds of the minimal portion of an array would make the entire
# array sorted if it were sorted.

def sub_sort(array):
  n = len(array)
  max_so_far = [max(array[:i+1]) for i in range(n)]
  min_so_far = [min(array[i:]) for i in range(n)]
  condition_results = [min_so_far[i] != max_so_far[i] for i in range(n)]

  # Finding the first occurrence where the condition is True
  start = condition_results.index(True) if True in condition_results else 0
  end = condition_results[::-1].index(True) if True in condition_results else n - 1

  # Adjusting end index because we reversed the list
  return start, n - end - 1    



class Test(unittest.TestCase):
  def test_sub_sort(self):
    array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    self.assertEqual(sub_sort(array), (0, 0))
    array = [10, 11, 12, 13, 14, 16, 15, 17, 18, 19]
    self.assertEqual(sub_sort(array), (5, 6))
    array = [10, 18, 12, 13, 14, 16, 15, 17, 11, 19]
    self.assertEqual(sub_sort(array), (1, 8))
    array = [90, 80, 70, 60, 50, 40, 30, 20, 10, 1]
    self.assertEqual(sub_sort(array), (0, 9))

if __name__ == "__main__":
  unittest.main()

