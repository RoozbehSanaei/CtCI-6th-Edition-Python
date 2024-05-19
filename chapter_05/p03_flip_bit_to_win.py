
'''
Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.
'''

def flip_bit_to_win(number):
    number_str = bin(number)[2:]
    
    max_cnt, cnt, cnt0 = 0, 0, 0
    i = len(number_str)
    
    while i:
        if int(number_str[i - 1]):
            cnt += 1
        else:
            if cnt0 == 0:
                temp_i = i
                cnt0 = 1
            else:
                max_cnt = max(cnt, max_cnt)
                i = temp_i
                cnt0 = 0
                cnt = 0

        i -= 1
    
    max_cnt = max(cnt, max_cnt)

    return max_cnt + 1


'''
    Convert to Binary: 
        Start by converting the given number into its binary string representation, excluding the '0b' prefix typically added by Python.

    Initialize Variables: Set up three variables:
        One to track the maximum length of the sequence of 1s found so far.
        One to count the current sequence of 1s.
        One to keep track of the number of 0s encountered in the current sequence.

    Iterate Through Binary String in Reverse: 
        Begin at the end of the binary string and work backwards.

    Process Each Bit:
        If the current bit is 1, increment the count of the current sequence.
        If the current bit is 0:
            If this is the first 0 encountered in the current sequence, mark its position and note that a 0 has been encountered.
            If this is the second 0 encountered, update the maximum length if the current sequence length is larger. Then, reset the counting process to start from the first 0 encountered.

    Edge Case Handling: 
        After the loop, update the maximum length one last time to account for sequences that extend to the end of the binary string.

    Account for Bit Flip: 
        Add 1 to the maximum length to account for the one bit that can be flipped from 0 to 1.

    Return Result: 
        The final result is the length of the longest sequence of 1s that can be achieved by flipping one 0 to 1 in the binary representation of the given number.
'''

def flip_bit_to_win(number):
    number_str = bin(number)[2:]
    
    max_cnt, cnt, cnt0 = 0, 0, 0
    i = len(number_str)
    
    while i:
        if int(number_str[i - 1]):
            cnt += 1
        else:
            if cnt0 == 0:
                temp_i = i
                cnt0 = 1
            else:
                max_cnt = max(cnt, max_cnt)
                i = temp_i
                cnt0 = 0
                cnt = 0

        i -= 1
    
    max_cnt = max(cnt, max_cnt)

    return max_cnt + 1




test_cases = [
    (0b0, 1),
    (0b111, 4),
    (0b10011100111, 4),
    (0b10110110111, 6),
    (0b11011101111, 8),
]
testable_functions = [flip_bit_to_win, flip_bit_to_win_alt]


def test_flip_bit_to_win():
    for fli_bit in testable_functions:
        for num, expected in test_cases:
            assert fli_bit(num) == expected


if __name__ == "__main__":
    test_flip_bit_to_win()
