import unittest
# Return the bounds of the contiguous sequence with the largest sum.

def contiguous_sequence(array):
  seq_start,seq_end,seq_sum,max_sum,bounds = 0,0,0,0,(0,0)
  for i,elem in enumerate(array):
    seq_sum += elem
    if (seq_sum<0):
      seq_start = i+1
      seq_sum = 0
    if (seq_sum>max_sum):
      max_sum = seq_sum
      seq_end = i+1
      bounds = (seq_start,seq_end)
  return bounds


class Test(unittest.TestCase):
  def test_contiguous_sequence(self):
    seq = [-1, -4, -54, -7, -8, -2, -4, -3, -9]
    self.assertEqual(contiguous_sequence(seq), (0, 0))
    seq = [-1, 4, 4, -7, 8, 2, -4, 3]
    self.assertEqual(contiguous_sequence(seq), (1, 6))
    seq = [-1, 4, 4, -7, 8, 2, -4, -3, 9]
    self.assertEqual(contiguous_sequence(seq), (1, 9))
    seq = [-1, -4, -54, -7, -8, 2, -4, -3, 9]
    self.assertEqual(contiguous_sequence(seq), (8, 9))

if __name__ == "__main__":
  unittest.main()

