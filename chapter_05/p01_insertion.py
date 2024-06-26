'''
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
'''




def bits_insertion(n, m, i, j):
    ones_left = -1 << (j + 1)  # shift 1s over to the left, before position j
    ones_right = (1 << i) - 1  # place 1s to the right of position i
    mask = ones_left | ones_right  # encapsulate 0s with the 1s from above
    cleared = n & mask  # zero bits in positions j through i
    moved = m << i  # shift m over i places, prepped for n insertion
    return cleared | moved  # answer is the value after insertion

'''
If a bit in m is 1, the corresponding bit in n is set to 1: n |= 1 << (idx + i).
If a bit in m is 0, the corresponding bit in n is cleared (set to 0): n &= ~(1 << (idx + i)).
'''


def bits_insertion_easy_to_understand(n, m, i, j):
    # do a liner search through the bits of M (from tail to head)
    # and if you find 1, do a bit insertion to N
    # if you find 0, clear idxth bit of N using a mask
    for idx in range(j - i + 1):
        if (m >> idx) & 1 != 0:
            # set bit
            n |= 1 << (idx + i)
        else:
            # clear bit
            mask = ~(1 << (idx + i))
            n &= mask

    return n


test_cases = [
    ((int("10000000000", 2), int("10011", 2), 2, 6), int("10001001100", 2)),
    ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2)),
]

testable_functions = [bits_insertion, bits_insertion_easy_to_understand]


def test_bits_insertion():
    for bits_insert in testable_functions:
        for (n, m, i, j), expected in test_cases:
            calculated = bits_insert(n, m, i, j)
            error_msg = f"{bits_insert.__name__}: {calculated:b} != {expected:b}"
            assert bits_insert(n, m, i, j) == expected, error_msg


if __name__ == "__main__":
    test_bits_insertion()
