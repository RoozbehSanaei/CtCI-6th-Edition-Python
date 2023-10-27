'''
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
'''

def bit_swap_required(a: int, b: int) -> int:
    # XOR (^) between a and b gives a number c where the bits that differ between a and b are set to 1.
    # For example, if a=1101 and b=1011, a ^ b would be 0110.
    count, c = 0, a ^ b
    
    # This loop counts the number of bits set to 1 in c.
    # Essentially, it counts the number of bits that need to be flipped to turn a into b.
    while c:
        # Increment count by 1 for each bit that is set to 1 in c.
        count += 1
        
        # Bitwise AND between c and (c - 1) turns off the rightmost 1 in c.
        # For example, if c is 0110, then c - 1 is 0101, and c & (c - 1) would be 0100.
        c = c & (c - 1)
    
    # Return the count of bits needed to be flipped to turn a into b.
    return count



def test_29_15() -> None:
    a = 0b11101  # 29
    b = 0b01111  # 15
    assert bit_swap_required(a, b) == 2
