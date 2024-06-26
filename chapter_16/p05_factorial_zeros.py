# Count the number of zeros at the end of a factorial.

def factorial_zeros(n):
  # Initialize a counter for the number of factors of 5 in n!.
  five_factors = 0

  # Continue the loop as long as n is greater than 4.
  while n > 4:
    # Divide n by 5. This step finds the number of multiples of 5, 25, 125, etc., in n!.
    n /= 5

    # Add the quotient to the five_factors. This counts how many times 5 is a factor in n!.
    five_factors += n

  # Return the total count of factors of 5 in n!.
  return five_factors


import unittest

class Test(unittest.TestCase):
  def test_factorial_zeros(self):
    self.assertEqual(factorial_zeros(4), 0)
    self.assertEqual(factorial_zeros(9), 1)
    self.assertEqual(factorial_zeros(10), 2)
    self.assertEqual(factorial_zeros(25), 6)
    self.assertEqual(factorial_zeros(55), 13)

if __name__ == "__main__":
  unittest.main()
