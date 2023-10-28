import unittest

'''
You can think of each permutation as a kind of "number," where each element or digit contributes to its lexicographic "value." Just like how you find the next integer by looking at the units place, tens place, hundreds place, etc., you do something similar to find the next permutation.

In the context of numbers, to get the smallest number that's greater than the current one, you'd:

    Start from the rightmost digit (least significant) and look for the first digit that can be incremented without rolling over to 0.
    Increment that digit by 1.
    Set all the digits to the right of that one to 0 (their minimum value).

For permutations:

    Start from the rightmost element and look for the first pair (a[i-1], a[i]) where a[i-1] < a[i] (equivalent to finding a digit you can increment).
    Swap a[i-1] with the smallest element greater than it that's to its right (like incrementing that digit).
    Reverse the elements to the right of a[i-1] to sort them in ascending order (like setting the digits to the right to their minimum value).
'''



def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
    return True


def is_matched_parentheses(ray):
    lst = []
    for c in ray:
        if c == "(":
            lst.append(c)
        if c == ")":
            if len(lst) < 1 or lst.pop() != "(":
                return False
    return True


def generate_parentheses_permutations_brute_force(number_of_pairs):
    starting_list = (["("] * number_of_pairs) + [")"] * number_of_pairs
    possibilities = ["".join(starting_list)]
    while next_permutation(starting_list):
        if is_matched_parentheses(starting_list):
            possibilities.append("".join(starting_list))
    return possibilities


def generate_parentheses_permutations_recursive_1(n):
    def helper(
        open_parentheses_remaining, closed_parentheses_remaining, current_string
    ):
        if len(current_string) == n * 2:
            result.append(current_string)
        if open_parentheses_remaining > 0:
            helper(
                open_parentheses_remaining - 1,
                closed_parentheses_remaining,
                current_string + "(",
            )
        if closed_parentheses_remaining > open_parentheses_remaining:
            helper(
                open_parentheses_remaining,
                closed_parentheses_remaining - 1,
                current_string + ")",
            )

    result = []
    helper(n, n, "")
    return result


def add_paren(arr, left_rem, right_rem, string_arr, idx):
    if left_rem < 0 or right_rem < left_rem:  # invalid
        return
    if left_rem == 0 and right_rem == 0:  # out of left and right parentheses
        elem = "".join(string_arr)
        arr.append(elem)

    else:
        string_arr[idx] = "("  # add left and recurse
        add_paren(arr, left_rem - 1, right_rem, string_arr, idx + 1)

        string_arr[idx] = ")"  # add right and recurse
        add_paren(arr, left_rem, right_rem - 1, string_arr, idx + 1)


def generate_parentheses_permutations_recursive_2(n):
    results = []
    string_arr = ["*"] * n * 2
    add_paren(results, n, n, string_arr, 0)
    return results


testable_functions = [
    generate_parentheses_permutations_brute_force,
    generate_parentheses_permutations_recursive_1,
    generate_parentheses_permutations_recursive_2,
]

test_cases = [
    (0, [""]),
    (1, ["()"]),
    (2, sorted(["()()", "(())"])),
    (3, sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])),
]


class TestSuite(unittest.TestCase):
    def test_generate_parentheses_permutations(self):
        for f in testable_functions:
            for num, expected in test_cases:
                assert sorted(f(num)) == expected, f"{f.__name__} {num} failed"


def example():
    print(generate_parentheses_permutations_recursive_1(2))
    print(generate_parentheses_permutations_brute_force(3))
    print(generate_parentheses_permutations_recursive_2(3))


if __name__ == "__main__":
    example()
