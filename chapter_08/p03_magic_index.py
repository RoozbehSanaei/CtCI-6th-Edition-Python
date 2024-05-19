NOT_FOUND = -1

'''
The algorithm is designed to find a "magic index" in a given array. 
A magic index in an array is defined as an index where the value at that index is equal to the index itself. 
    
    Initial Setup:
        The algorithm begins by checking if the maximum index for the search is not defined. 
        If it's not defined, it sets the maximum index to the last index of the array.
        It then checks if the maximum index is less than the minimum index. If it is, this indicates that the entire array has been searched without finding a magic index, and the algorithm returns a signal indicating that a magic index was not found.

    Binary Search for Magic Index:
        The algorithm employs a binary search approach to efficiently find the magic index.
        It calculates the middle index of the current search range.
        It then checks if the value at this middle index is equal to the index itself. If it is, the algorithm concludes that this is the magic index and returns this index.

    Recursive Search in Subarrays:
        If the value at the middle index is less than the middle index, the algorithm concludes that if a magic index exists, 
        it must be in the subarray to the right of the middle index. 
        It then recursively calls itself to search this right subarray.
        Conversely, if the value at the middle index is greater than the middle index, the algorithm concludes that if a magic index exists, 
        it must be in the subarray to the left of the middle index. It then recursively calls itself to search this left subarray.

    Concluding the Search:
        The algorithm continues this process of dividing the array and searching the relevant subarrays until it either finds a magic index or concludes that no magic index exists in the array.

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
nitial Setup:

    The algorithm begins by setting the maximum index to the last index of the array if it's not already specified.
    It then checks if the search range is valid. If the maximum index is less than the minimum index, it means the entire array has been searched without finding a magic index, and the algorithm returns a signal indicating that a magic index was not found.

Finding the Middle Index:

    The algorithm calculates the middle index of the current search range.

Checking for Magic Index:

    It checks if the element at the middle index is equal to the middle index itself. If they are equal, the algorithm concludes that this index is the magic index and returns it.

If the magic index is not found at the middle, the algorithm then searches recursively:

Recursive Search in the Right Subarray:

    It calculates the left boundary for the search, which is the smaller of the middle index minus one and the value at the middle index.
    The algorithm then recursively searches for the magic index in this left subarray.
    If a magic index is found in the left subarray, it is returned.

Recursive Search in the Right Subarray:

    If no magic index is found in the left subarray, the algorithm proceeds to search the right subarray.
    It calculates the right boundary for the new search range, which is the larger of the middle index plus one and the value at the middle index.
    The algorithm then recursively searches for the magic index in this right subarray.

Concluding the Search:

    The algorithm continues this process of dividing the array and searching the relevant subarrays until it either finds a magic index or concludes that no magic index exists in the array.
'''

def magic_index_non_distinct(array, min_index=0, max_index=None):
    if max_index is None:
        max_index = len(array) - 1

    if max_index < min_index:
        return NOT_FOUND

    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid

    left_index = min(mid - 1, array[mid])
    left = magic_index_non_distinct(array, min_index, left_index)
    if left >= 0:
        return left

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
