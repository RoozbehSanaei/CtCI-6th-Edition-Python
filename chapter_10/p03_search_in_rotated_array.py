from typing import Optional, Sequence

'''



    The function index, which finds the index of a target element in a rotated sorted array,  . Essentially, it's a sorted array in which the starting elements have been moved to the end. 
    For example, if you take a sorted array like [0, 1, 2, 4, 5, 6, 7] and rotate it by two positions, it becomes [4, 5, 6, 7, 0, 1, 2]:

    
    
    Check for an Empty Array:
      Initially, the function checks if the array nums is empty. If it is, the function returns None, indicating that the search is not possible.  In this case, it's not, so we proceed.

    Handle Duplicate Edge Cases: 
        If the first and last elements of the array are the same (like [1, 2, 3, 1, 1]), the array might contain duplicates. 
        In this case, the function performs a linear search to find the target element. If the target is found, its index is returned; otherwise, None is returned.
        Our array is [4, 5, 6, 7, 0, 1, 2], and the first and last elements (4 and 2) are not the same, so we skip the linear search part.

    Determine Target's Relative Position: 
        The function then checks if the target value is greater than or equal to the first element of the array and keepts in a flag. 
    This helps in understanding if the target lies to the left or right of the smallest element (the point where the sorted array was rotated).
    We check if the target (0) is greater than or equal to the first element (4). It's not, so we know our target is to the right of the smallest element, which is after the rotation point.

    Set Up for Binary Search: 
        Two pointers, lo (low) and hi (high), are initialized to point at the start and end of the array, respectively. These pointers help in narrowing down the search space.
        We set lo = 0 and hi = 6 (array length minus one).

    Perform Binary Search: The function then enters a loop to perform a binary search:
        It calculates the middle index (mid) of the current search space.
        It checks if the middle element is on the same side as the first element of the array. This step determines whether the middle element is to the left or right of the rotation point in the array.
        Depending on the position of the middle element and the target element relative to the rotation point, the function adjusts the lo and hi pointers:
            If the middle element and target are on different sides of the rotation point, the search space is adjusted to the half where the target must be.
            If both are on the same side, it follows the standard binary search process. If the middle element is less than the target, it narrows the search to the right half; if greater, to the left half.
        This process repeats until the target is found (in which case its index is returned) or the search space is exhausted (returning None).

        Iteration   lo  hi  mid Mid Element  Action Taken
        1           0   6   3   7            Set lo to mid + 1 (4) because 7 (mid element) is greater than 0 (target), and 7 is on the left side of rotation while 0 is on the right side (0<4)
        2           4   6   5   1            Set hi to mid - 1 (4) because 1 (mid element) is greater than 0 (target)
        3           4   4   4   0            Target found at mid; 0 (mid element) equals 0 (target)



'''

def index(nums: Sequence[int], target: int) -> Optional[int]:
    if not nums:
        return None
    
    if nums[0] == nums[-1]:
        try:
            return nums.index(target)
        except ValueError:
            return None
    
    is_target_left_of_wraparound = target >= nums[0]
    
    lo, hi = 0, len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        is_mid_left_of_wraparound = nums[mid] >= nums[0]
        
        if is_mid_left_of_wraparound and not is_target_left_of_wraparound:
            lo = mid + 1
        elif not is_mid_left_of_wraparound and is_target_left_of_wraparound:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            return mid
            
    return None


'''
    Initial Check: First, the function checks if the input array is empty. If it is, it returns None, indicating the target cannot be found in an empty array.

    Recursive Search Invocation: If the array is not empty, it calls the _recursive_search function with the full array and the target number, along with the start (0) and end (length of the array minus 1) indices.

    Finding the Middle: In _recursive_search, it calculates the middle index of the current search range.

    Base Cases:
        If the element at the middle index equals the target number, the index is returned, as the target is found.
        If the search range is reduced to zero (start index equals end index), and the target is not found, return None.

    Determining Sorted Half:
        The algorithm checks if the left half of the array is sorted (from start to middle). If the target lies within this range, the search continues recursively in this half.
        If the right half (from middle to end) is sorted and the target lies within this range, the search continues recursively in this half.
        If there are duplicates and it's unclear which half is sorted, the algorithm needs to handle this scenario by checking both halves.

    Recursive Calls: Depending on the scenario, _recursive_search is called recursively with updated start and end indices, narrowing down the search range each time.

    Returning the Result: Once the target is found, its index is returned. If not found in any recursive calls, None is returned.

    array[start] < array[middle] | array[middle] < array[end] | array[start] == array[middle] | array[start] <= num < array[middle] | array[middle] < num <= array[end] | array[middle] != array[end] | Recursion Call
    True                         | -                           | -                             | True                              | -                                    | -                               | _recursive_search(array, num, start, middle - 1)
    True                         | -                           | -                             | False                             | -                                    | -                               | _recursive_search(array, num, middle + 1, end)
    -                            | True                        | -                             | -                                 | True                                 | -                               | _recursive_search(array, num, middle + 1, end)
    -                            | True                        | -                             | -                                 | False                                | -                               | _recursive_search(array, num, start, middle - 1)
    -                            | -                           | True                          | -                                 | -                                    | True                            | _recursive_search(array, num, middle + 1, end)
    -                            | -                           | True                          | -                                 | -                                    | False                           | _recursive_search(array, num, start, middle - 1), then if result is None, _recursive_search(array, num, middle + 1, end)

    

    Recursive Call | Start Index | End Index | Middle Index | Middle Element | Action Taken
    1              | 0           | 6         | 3            | 7              | Since 7 (mid element) is greater than 0 (target), and target could be in the right half [0, 1, 2], search right
    2              | 4           | 6         | 5            | 1              | Since 1 (mid element) is greater than 0 (target), continue search in left part of this half
    3              | 4           | 4         | 4            | 0              | Target 0 found at middle index





'''

def search_rotated(array: Sequence[int], num: int) -> Optional[int]:
    if not array:
        return None
    return _recursive_search(array, num, 0, len(array) - 1)

def _recursive_search(array, num, start, end):
    middle = (end - start) // 2 + start
    if array[middle] == num:
        return middle
    if end - start <= 0:
        return None
    result = None
    if array[start] < array[middle]:
        if array[start] <= num < array[middle]:
            result = _recursive_search(array, num, start, middle - 1)
        else:
            result = _recursive_search(array, num, middle + 1, end)
    elif array[middle] < array[end]:
        if array[middle] < num <= array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        else:
            result = _recursive_search(array, num, start, middle - 1)
    elif array[start] == array[middle]:
        if array[middle] != array[end]:
            result = _recursive_search(array, num, middle + 1, end)
        else:
            result = _recursive_search(array, num, start, middle - 1)
            if result is None:
                result = _recursive_search(array, num, middle + 1, end)
    return result




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
