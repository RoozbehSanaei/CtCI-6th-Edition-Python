
'''
Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.
'''

def flip_bit_to_win(number):
    # Convert the number to a binary string
    number_str = bin(number)[2:]
    
    # Initialize variables to keep track of the longest sequence,
    # the current sequence, and the number of zeros encountered
    max_cnt, cnt, cnt0 = 0, 0, 0
    
    # Start index for iterating through the binary string in reverse
    i = len(number_str)
    
    # Loop through the binary string in reverse
    while i:
        # Check if the current bit is 1
        if int(number_str[i - 1]):
            cnt += 1  # Increment the current sequence length
        else:
            # Check if this is the first zero encountered
            if cnt0 == 0:
                temp_i = i  # Save the index of the first zero
                cnt0 = 1    # Mark that we've encountered a zero
            else:  # This is the second zero encountered
                max_cnt = max(cnt, max_cnt)  # Update the longest sequence
                i = temp_i  # Rewind to the first zero
                cnt0 = 0  # Reset the zero counter
                cnt = 0  # Reset the current sequence length
        
        i -= 1  # Move to the previous bit
    
    # Update the longest sequence one last time to consider the edge case
    max_cnt = max(cnt, max_cnt)
    
    # Add 1 to account for the zero that can be flipped
    return max_cnt + 1

def flip_bit_to_win_alt(num):
    # Initialize variables for the longest sequence,
    # the current sequence of 1s, and the past sequence of 1s
    longest, current_segment, past_segment = 1, 0, 0
    
    # Continue the loop as long as num is not 0
    while num != 0:
        if num & 1:  # Check if the current bit is 1
            current_segment += 1  # Increment the count for the current sequence
        else:  # If the current bit is 0
            # Check if the next bit is also 0; if so, reset past_segment to 0
            # Otherwise, set past_segment to the length of the current_segment
            past_segment = 0 if (num & 2) else current_segment
            current_segment = 0  # Reset the count for the current sequence
        
        # Update the longest sequence; add 1 for the bit that can be flipped
        longest = max(current_segment + past_segment + 1, longest)
        
        num >>= 1  # Right-shift num to check the next bit
        
    return longest  # Return the length of the longest sequence of 1s

# Test the function
print(flip_bit_to_win_alt(0b11011101111))  # Should output 8



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
