'''
Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball,{"at",
""}'
'''

'''
Top-Level Function - sparse_search:
    Purpose: Initiates the search process for a specific item in a sparse sorted array.
    Process:
        Calls a nested inner function, inner_search, passing the entire range of the array for the initial search.

Nested Function for Binary Search - inner_search:
    Purpose: 
        Handles the binary search within the array, accommodating for sparse elements (empty strings).
    Process:
        Initialization: 
            Starts with low and high indices defining the current search range.
        Finding the Middle Element:
            Calculates the middle index of the current range.
            If the middle element is an empty string, searches for the nearest non-empty string.
        Handling Sparse Elements:
            Initializes two pointers, left and right, around the middle index.
            Expands these pointers outward until a non-empty string is found or the pointers go out of bounds.
            Updates the middle index to the index of the first non-empty string found.
        Binary Search Logic:
            If a non-empty middle element is found, compares it with the target item.
            Base Case: If the item matches, returns its index.
            Recursive Steps:
                If the item is smaller than the middle element, recursively searches the left half of the current range.
                If the item is larger, recursively searches the right half.

Returning the Result:
    The recursive search either finds the item and returns its index or concludes that the item is not in the array, returning None.
'''

def sparse_search(arr, item):
    def inner_search(arr, item, low, high):
        middle = ((high - low) // 2) + low

        if arr[middle] == "":
            left = middle - 1
            right = middle + 1

            while True:
                if left < low and right > high:
                    return None
                elif right <= high and arr[right] != "":
                    middle = right
                    break
                elif left >= low and arr[left] != "":
                    middle = left
                    break
                left -= 1
                right += 1

        if arr[middle] == item:
            return middle
        if arr[middle] > item:
            return inner_search(arr, item, low, middle - 1)
        if arr[middle] < item:
            return inner_search(arr, item, middle + 1, high)

    return inner_search(arr, item, 0, len(arr) - 1)


test_cases = [
    ((["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "d"), 8),
    ((["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "f"), None),
    ((["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "a"), 0),
]

testable_functions = [sparse_search]


def test_sorted_search():
    for function in testable_functions:
        for (n, m), expected in test_cases:
            calculated = function(n, m)
            error_msg = f"{function.__name__}: {calculated} != {expected}"
            assert function(n, m) == expected, error_msg


if __name__ == "__main__":
    test_sorted_search()
