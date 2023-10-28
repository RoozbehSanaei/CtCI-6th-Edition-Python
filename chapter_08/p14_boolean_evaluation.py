import unittest


'''
Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), I (OR), and /\ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result.
EXAMPLE
'''


def string_to_bool(s: str) -> bool:
    return s == "1"


# Define the function count_ways which takes an expression string 'exp', a boolean 'result', and a memoization dictionary 'memo'
def count_ways(exp: str, result: bool, memo) -> int:
    # Base case: if the expression is empty, return 0
    if len(exp) == 0:
        return 0
    # Base case: if the expression is a single character, check if it evaluates to 'result'
    if len(exp) == 1:
        return 1 if string_to_bool(exp) == result else 0  # 'string_to_bool' function needs to be defined elsewhere
    
    # Check if the result for this sub-expression is already memoized
    if exp + str(result) in memo:
        return memo[exp + str(result)]

    # Initialize the count of ways to make the expression true to 0
    ways = 0

    # Loop through the expression, skipping operands and considering only operators
    for i in range(1, len(exp), 2):
        # Split the expression into left and right parts based on the current operator
        left = exp[:i]
        right = exp[i + 1:]

        # Calculate the number of ways to make the left and right sub-expressions true and false
        left_true = count_ways(left, True, memo)
        left_false = count_ways(left, False, memo)
        right_true = count_ways(right, True, memo)
        right_false = count_ways(right, False, memo)

        # Calculate the total number of ways to arrange the sub-expressions
        total = (left_true + left_false) * (right_true + right_false)

        # Initialize the count of ways to make the entire expression true to 0
        total_true = 0

        # Calculate the number of ways to make the entire expression true based on the current operator
        if exp[i] == "|":
            total_true = (
                left_true * right_true
                + left_false * right_true
                + left_true * right_false
            )
        elif exp[i] == "&":
            total_true = left_true * right_true
        elif exp[i] == "^":
            total_true = left_true * right_false + left_false * right_true

        # Calculate the number of ways to make the entire expression evaluate to 'result'
        subways = total_true if result else (total - total_true)
        ways += subways

    # Memoize the result for this sub-expression and return it
    memo[exp + str(result)] = ways
    return ways



def evaluate(exp: str, result: bool) -> int:
    memo = {}
    return count_ways(exp, result, memo)


class Test(unittest.TestCase):
    test_cases = [("1^0|0|1", False, 2), ("0&0&0&1^1|0", True, 10)]
    testable_functions = [evaluate]

    def test_evaluate(self):
        for f in self.testable_functions:
            for [expression, result, expected] in self.test_cases:
                assert f(expression, result) == expected


if __name__ == "__main__":
    unittest.main()
