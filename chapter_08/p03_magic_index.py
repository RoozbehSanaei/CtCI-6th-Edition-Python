NOT_FOUND = -1

'''
Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
'''

def magic_index(array, min_index=0, max_index=None):
    if max_index is None:
        max_index = len(array) - 1

    if max_index < min_index:
        return NOT_FOUND

    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return magic_index(array, mid + 1, max_index)
    if array[mid] > mid:
        return magic_index(array, min_index, mid - 1)

'''
all indices greater than array[mid] on the left sub-array cannot be magic indices because 
they would have values greater than their indices (since the array is sorted). Similarly
all indices less than array[mid] on the right sub-array cannot be magic indices. 
This is because the values at those indices would be smaller than their corresponding index (since the array is sorted).
'''


def magic_index_non_distinct(array, min_index=0, max_index=None):
    if max_index is None:
        max_index = len(array) - 1

    if max_index < min_index:
        return NOT_FOUND

    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid

    # Search left recursively
    left_index = min(mid - 1, array[mid])
    left = magic_index_non_distinct(array, min_index, left_index)
    if left >= 0:
        return left

    # Search right recursively
    right_index = max(mid + 1, array[mid])
    return magic_index_non_distinct(array, right_index, max_index)


test_cases = [
    ([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25], 5),
    ([-14, -12, 0, 1, 2, 7, 9, 10, 23, 25], NOT_FOUND),
    ([0, 1, 2, 3, 4], 2),
    ([], NOT_FOUND),
]

followup_test_cases = test_cases + [
    ([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 2),
]


def test_magic_index():
    for array, expected in test_cases:
        assert magic_index(array) == expected


def test_magic_index_non_distinct():
    for array, expected in followup_test_cases:
        assert magic_index_non_distinct(array) == expected


if __name__ == "__main__":
    test_magic_index()
    test_magic_index_non_distinct()
