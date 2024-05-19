
'''
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''

'''
Function triple_hop:

    If x is less than 0, meaning it's not a valid step count, return 0 as there are no ways to hop negative steps.
    If x is exactly 0, return 1 because there is one way to stay where you are (no hops needed).
    If x is 1, return 1 as there's only one way to hop a single step.
    For any other value of x, the function calls itself recursively to calculate the sum of:
        The number of ways to reach the step that's one hop away (x - 1),
        The number of ways to reach the step that's two hops away (x - 2), and
        The number of ways to reach the step that's three hops away (x - 3).
    This recursive approach calculates all possible combinations of 1, 2, and 3 step hops to reach the top.
'''
def triple_hop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)

'''
Function triple_hop_recursive_memo:

    This function serves as a wrapper for a more efficient version of the triple_hop calculation, using memoization to store previously calculated results.
    It initializes a list memo with -1 to indicate that the number of ways to reach each step has not been calculated yet. 
    The size of this list is x + 1, accommodating all steps from 0 to x.
    It then calls the triple_hop_recursive function, passing the number of steps x and the memo list.

Function triple_hop_recursive:

    This function is similar to triple_hop but uses the memo list to store and retrieve calculated values, reducing the number of recursive calls.
    If x is less than 0, return 0 as there are no valid steps.
    Set memo[0] to 1, as there is only one way to stay at the starting point.
    If x is at least 1, set memo[1] to 1, as there's only one way to hop a single step.
    If x is at least 2, calculate memo[2] as the sum of memo[1] and memo[0].
    For x greater than 2, iterate through the steps from 3 to x, and for each step i, calculate memo[i] as the sum of the ways to reach the three preceding steps. 
    This uses the stored values in memo to avoid redundant calculations.
    Finally, return the value of memo[x], which is the number of ways to reach step x.
'''

def triple_hop_recursive_memo(x):
    memo = [-1] * (x + 1)
    return triple_hop_recursive(x, memo)


def triple_hop_recursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]


if __name__ == "__main__":
    print(triple_hop(1))
    print(triple_hop(2))
    print(triple_hop(3))
    print(triple_hop(4))
    print(triple_hop(5))
    print(triple_hop(6))

    print(method_2(1))
    print(method_2(2))
    print(method_2(3))
    print(method_2(4))
    print(method_2(5))
    print(method_2(6))
