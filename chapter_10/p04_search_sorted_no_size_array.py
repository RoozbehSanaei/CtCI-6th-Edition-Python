'''
You are given an array like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
'''

'''
Exponential Backoff in sorted_nosize_search: 
    This part aims to determine a suitable range where the desired number (num) may exist in the sorted array (listy). 
    It starts from the beginning of the array and exponentially jumps indices until it either finds a number larger than num 
    or hits an IndexError, indicating the end of the array. This step sets the stage for a more focused search.
'''

def sorted_nosize_search(listy, num):
    # Adapted to work with a Python sorted
    # array and handle the index error exception
    exp_backoff = index = 0
    limit = False
    while not limit:
        try:
            temp = listy[index]
            if temp > num:
                limit = True
            else:
                index = 2**exp_backoff
                exp_backoff += 1
        except IndexError:
            limit = True
    return bi_search(listy, num, index // 2, index)


def bi_search(listy, num, low, high):
    while low <= high:
        middle = (high + low) // 2

        try:
            value_at = listy[middle]
        except IndexError:
            value_at = -1

        if num < value_at or value_at == -1:
            high = middle - 1
        elif num > value_at:
            low = middle + 1
        else:
            return middle
    return -1


test_cases = [
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 0), -1),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 1), 0),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 2), 1),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), 2),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), 3),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 4),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 6), 5),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 7), 6),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 7),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 8),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1),
]

testable_functions = [sorted_nosize_search]


def test_sorted_search():
    for function in testable_functions:
        for (n, m), expected in test_cases:
            calculated = function(n, m)
            error_msg = f"{function.__name__}: {calculated} != {expected}"
            assert function(n, m) == expected, error_msg


if __name__ == "__main__":
    test_sorted_search()
