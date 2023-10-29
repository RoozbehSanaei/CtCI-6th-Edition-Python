from typing import Optional, Sequence

# Function to find the index of a target element in a rotated sorted array
def index(nums: Sequence[int], target: int) -> Optional[int]:
    # Handle the case where the input array is empty
    if not nums:
        return None
    
    # Special case: if the first and last elements are the same, 
    # we can't do better than O(n). We do a linear search in this case.
    if nums[0] == nums[-1]:
        try:
            return nums.index(target)
        except ValueError:
            return None
    
    # Determine if the target is to the left of the "wrap-around" point (smallest element)
    is_target_left_of_wraparound = target >= nums[0]
    
    # Initialize pointers for binary search
    lo, hi = 0, len(nums) - 1
    
    # Binary search loop
    while lo <= hi:
        # Calculate mid-point
        mid = (lo + hi) // 2
        # Determine if the middle element is to the left of the "wrap-around" point
        is_mid_left_of_wraparound = nums[mid] >= nums[0]
        
        # Check if the middle element is to the left of the "wrap-around" point,
        # and the target is to the right of the "wrap-around" point.
        if is_mid_left_of_wraparound and not is_target_left_of_wraparound:
            lo = mid + 1  # Move the lower bound to mid + 1 to search the right half
            
        # Check if the middle element is to the right of the "wrap-around" point,
        # and the target is to the left of the "wrap-around" point.
        elif not is_mid_left_of_wraparound and is_target_left_of_wraparound:
            hi = mid - 1  # Move the upper bound to mid - 1 to search the left half

        # Regular binary search conditions below
        elif nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            # Target found
            assert nums[mid] == target
            return mid
            
    # Target not found
    return None



def search_rotated(array: Sequence[int], num: int) -> Optional[int]:
    if not array:
        return None
    return _recursive_search(array, num, 0, len(array) - 1)


# Recursive function to search for a number in a rotated sorted array
def _recursive_search(array, num, start, end):
    # Calculate the middle index of the current search range
    middle = (end - start) // 2 + start
    
    # Base case: If we find the target number, return its index
    if array[middle] == num:
        return middle
    
    # Base case: If the search range is empty, the number is not in the array
    if end - start <= 0:
        return None
    
    result = None  # Initialize result as None
    
    
    # Case 1: Left half of the array is sorted: 
    if array[start] < array[middle]:
        # If the number is in the sorted range, search only in that half
        if array[start] <= num < array[middle]:
            result = _recursive_search(array, num, start, middle - 1)
        # Otherwise, search in the other half
        else:
            result = _recursive_search(array, num, middle + 1, end)
            
    # Case 2: Right half of the array is sorted
    elif array[middle] < array[end]:
        # If the number is in the sorted range, search only in that half
        if array[middle] < num <= array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        # Otherwise, search in the other half
        else:
            result = _recursive_search(array, num, start, middle - 1)
    
    # Case 3: Duplicates are present, and we don't know which half is sorted
    elif array[start] == array[middle]:
        # If the middle element is different from the end, the right half is sorted
        if array[middle] != array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        # Otherwise, we must search in both halves
        else:
            result = _recursive_search(array, num, start, middle - 1)
            if result is None:
                result = _recursive_search(array, num, middle + 1, end)
    
    return result  # Return the result



test_cases = [
    # array, target, valid solutions
    ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 2, {0, 3, 4, 5, 6, 7, 8, 9}),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 3, 1),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 4, None),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 1, 2),
    ([2, 3, 1, 2, 2, 2, 2, 2, 2, 2], 8, None),
]

testable_functions = [index, search_rotated]


def test_index():
    for array, target, expected in test_cases:
        for method in testable_functions:
            ind = method(array, target)
            if isinstance(expected, set):
                assert ind in expected
            else:
                error_msg = (
                    f"arr:{array} target:{target} calculated:{ind} expected:{expected}"
                )
                assert ind == expected, error_msg


if __name__ == "__main__":
    test_index()
