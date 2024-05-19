import unittest
# Return the index of two numbers which could be swapped to make the sum of
# the two arrays equal.

def equalize_sum_with_swap(arr1, arr2):
    sum1, sum2 = sum(arr1), sum(arr2)
    if (sum1 - sum2) % 2 != 0:
        return None
    
    target_diff = (sum1 - sum2) / 2
    arr2_inverse = {num + target_diff: idx for idx, num in enumerate(arr2)}

    for idx, num in enumerate(arr1):
        if num in arr2_inverse:
            return idx, arr2_inverse[num]
    
    return None




class Test(unittest.TestCase):
  def test_equalize_sum_with_swap(self):
    arr1 = [5, 5, 10]
    arr2 = [4, 4, 8]
    swap = equalize_sum_with_swap(arr1, arr2)
    print(swap)
    arr1 = [5, 5, 5]
    arr2 = [6, 4, 6]
    swap = equalize_sum_with_swap(arr1, arr2)
    print(swap)
    arr1 = [5, 5, 14]
    arr2 = [7, 7, 8]
    swap = equalize_sum_with_swap(arr1, arr2)
    print(swap)
    arr1 = [5, 5, 14]
    arr2 = [4, 10, 8]
    swap = equalize_sum_with_swap(arr1, arr2)
    print(swap)

if __name__ == "__main__":
  unittest.main()

