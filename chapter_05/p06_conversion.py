'''
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
'''

'''
    Calculate Differences in Bits:
        Start by performing a bitwise XOR operation between the two integers, a and b. 
        This operation will produce a result where each bit is set to 1 if the corresponding bits in a and b are different, and 0 if they are the same. 
        For example, if a is 1101 and b is 1011, the XOR result will be 0110, indicating the positions where a and b differ.

    Count the Number of Differences:
        Initialize a counter to keep track of how many bits differ between a and b.
        
        The while loop in the function counts and eliminates each differing bit between two numbers, 
        continuing until no differing bits remain. This count represents the total bit flips required to convert one number into the other.
            Increment the counter by 1. This step counts one differing bit:
            Update the XOR result by performing a bitwise AND operation between the current XOR result and one less than the current XOR result. 
            This operation turns off the rightmost set bit (changing it from 1 to 0). 
            For instance, if the current XOR result is 0110, subtracting 1 gives 0101, and the AND operation of 0110 & 0101 results in 0100. 
            This step effectively removes the rightmost set bit from the XOR result.

    Return the Count:
        After processing all bits, the counter will reflect the total number of bits that need to be flipped to convert a into b.
        Return this count as the result.

'''

def bit_swap_required(a: int, b: int) -> int:
    count, c = 0, a ^ b
    
    while c:
        count += 1
        c = c & (c - 1)

    return count



def test_29_15() -> None:
    a = 0b11101  # 29
    b = 0b01111  # 15
    assert bit_swap_required(a, b) == 2
