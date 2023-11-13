import sys

# Function to sort the arrays in O(nlog(n))
def merge_sort(arr):
    # Function to recursively divide the array into smaller parts
    def make_partition(_arr):
        # Base case: if the array has 0 or 1 element, it's already sorted
        if len(_arr) <= 1:
            return _arr
        # Find the middle index for splitting the array
        middle = len(_arr) // 2
        # Recursively partition the left half
        left = make_partition(_arr[:middle])
        # Recursively partition the right half
        right = make_partition(_arr[middle:])
        # Merge the sorted halves
        return merge_partition(left, right)

    # Function to merge two sorted arrays into one sorted array
    def merge_partition(left, right):
        result = []  # Initialize an empty array to store the merged result
        i, j = 0, 0  # Initialize pointers for left and right arrays
        # Merge elements from left and right arrays in sorted order
        while i < len(left) and j < len(right):
            # Append the smaller element to the result
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Append any remaining elements from the left array
        result += left[i:]
        # Append any remaining elements from the right array
        result += right[j:]
        return result

    # Start the partitioning process
    return make_partition(arr)

# Function to find the smallest difference between elements of two arrays
def find_smallest_difference(array1, array2):
    # Sort both arrays using merge sort
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    # Initialize pointers and the minimum difference found so far
    a, b, difference = 0, 0, sys.maxsize
    pair = []  # To store the pair of elements with the smallest difference

    # Iterate through both arrays to find the smallest difference
    while a < len(array1) and b < len(array2):
        # Update the smallest difference and the corresponding pair of elements
        if abs(array1[a] - array2[b]) < difference:
            difference = abs(array1[a] - array2[b])
            pair = [array1[a], array2[b]]
            # If the difference is zero, it's the smallest possible, so break
            if difference == 0:
                break
        # Move the pointer in the array with the smaller current element
        if array1[a] < array2[b]:
            a += 1
        else:
            b += 1

    # Return the smallest difference and the corresponding pair
    return difference, pair

def test_find_smallest_diff():
    test_cases = [
        [[1, 3, 15, 11, 2], [23, 127, 235, 19, 8], (3, [11, 8])],
        [[2, 11, 15, 1], [12, 4, 235, 19, 127, 23], (1, [11, 12])],
        [[32, 1, 5, -31], [98, 7, 32, 43, 72, 86], (0, [32, 32])],
    ]
    for a, b, expected in test_cases:
        assert find_smallest_difference(a, b) == expected
