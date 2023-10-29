'''
Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball,{"at",
""}'
'''

def sparse_search(arr, item):
    # Inner function to handle the actual binary search
    def inner_search(arr, item, low, high):
        # Calculate the middle index
        middle = ((high - low) // 2) + low

        # Check if the middle element is an empty string
        if arr[middle] == "":
            # Initialize pointers for left and right of middle
            left = middle - 1
            right = middle + 1

            # Search for the nearest non-empty string in the array
            while True:
                # If both left and right pointers go out of bound, return None
                if left < low and right > high:
                    return None
                # If right pointer is within bound and points to a non-empty string, update middle
                elif right <= high and arr[right] != "":
                    middle = right
                    break
                # If left pointer is within bound and points to a non-empty string, update middle
                elif left >= low and arr[left] != "":
                    middle = left
                    break
                # Move the pointers
                left -= 1
                right += 1

        # Standard binary search logic from this point
        if arr[middle] == item:
            return middle  # Found the item, return its index
        if arr[middle] > item:
            return inner_search(arr, item, low, middle - 1)  # Continue search in lower half
        if arr[middle] < item:
            return inner_search(arr, item, middle + 1, high)  # Continue search in upper half

    # Initial call to the inner_search function with the full array range
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
