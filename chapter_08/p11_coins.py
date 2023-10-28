STANDARD_COIN_SIZES = [1, 5, 10, 25]

'''
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
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

    '''
    The total number of ways to make change for amount is the sum of the ways to make change without the last coin and the ways to make change with the last coin
    "last coin" specifically refers to the coin of size coin_sizes[m - 1], which is the last coin in the list of coin_sizes.
    '''
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
