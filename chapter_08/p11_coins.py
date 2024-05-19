STANDARD_COIN_SIZES = [1, 5, 10, 25]

'''
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''

'''
    The function is designed to calculate the number of different combinations of coins that can sum up to a specific amount.
    It takes two parameters: the total amount for which combinations are to be found, and an optional list of coin denominations.

    Base Cases:
        If the amount is exactly 0, the function returns 1, indicating there is one way to make the amount (using no coins).
        If the amount is less than 0, it returns 0, as it's not possible to make a negative amount with coins.
        If no list of coin denominations is provided, a standard set of coin sizes is used.

    Recursive Computation:
        The function first checks if there are any coin denominations left to consider. If not, it returns 0, as it's impossible to make the amount with no coin denominations.
        The function then splits the problem into two parts, each solved recursively:
            The first part calculates the number of combinations without using the last coin denomination in the list.
            The second part calculates the number of combinations that include at least one of the last coin denomination. It does this by reducing the amount by the value of this coin and recalculating the combinations for the new amount with the same set of coin denominations.

    Combining Results:
        The final result is the sum of the results from these two recursive calls.
        By continuously dividing the problem into smaller sub-problems (considering fewer coin denominations and smaller amounts), the function eventually calculates the total number of combinations that can make up the original amount with the given set of coin denominations.

'''

def coin_combinations(amount, coin_sizes=None):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if coin_sizes is None:
        coin_sizes = STANDARD_COIN_SIZES

    if len(coin_sizes) == 0:
        return 0
    m = len(coin_sizes)

    return coin_combinations(amount, coin_sizes[: m - 1]) + coin_combinations(
        amount - coin_sizes[m - 1], coin_sizes
    )


def coin_combinations_iterative(amount, coin_sizes=None):
    table = [0] * (amount + 1)
    # first case 0 value
    table[0] = 1

    if coin_sizes is None:
        coin_sizes = STANDARD_COIN_SIZES
    for i in range(0, len(coin_sizes)):
        for j in range(coin_sizes[i], amount + 1):
            table[j] += table[j - coin_sizes[i]]
    return table[amount]


if __name__ == "__main__":
    print(coin_combinations(100))
    print(coin_combinations_iterative(100))
