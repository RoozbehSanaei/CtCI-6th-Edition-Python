'''
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''

'''

The pairwise_swap function performs a pairwise swap of the bits in a given integer. Here's a description of the algorithm in natural language:

    Create Bitmasks:
        Generate a bitmask to isolate all even bits (bits in positions 0, 2, 4, etc.). 
        This is done using a hexadecimal number where all even positions are set to 1 (represented by 0xAAAAAAAA).
        Generate another bitmask to isolate all odd bits (bits in positions 1, 3, 5, etc.). 
        This bitmask is the inverse of the first one, with 1s in odd positions (represented by 0x55555555).

        
    Isolate Even and Odd Bits:
        Apply the even bitmask to the number using a bitwise AND operation.
        This zeroes out all the odd bits, leaving only the even bits.
        Similarly, apply the odd bitmask to the number to zero out all the even bits, leaving only the odd bits.

    Shift Bits:
        Shift the isolated even bits to the right by one position. This moves them into the places where the odd bits were.
        Shift the isolated odd bits to the left by one position, moving them into the places where the even bits were.

    Combine Shifted Bits:
        Perform a bitwise OR operation between the shifted even bits and shifted odd bits.
        This combines them into a single number with the original even and odd bits swapped pairwise.
'''

def pairwise_swap(number):
    mask_10 = 0xAAAAAAAA
    mask_01 = 0x55555555
    
    num_evn = number & mask_10
    num_odd = number & mask_01
    
    swp_num = (num_evn >> 1) | (num_odd << 1)
    
    return swp_num



def test_pairwise_swap():
    view_output = 1
    for number, exp_output in zip([123, 781, 278], [183, 782, 553]):
        swap_num = pairwise_swap(number)
        if view_output:
            print(f"Number:  {bin(number)}")
            print(f"Swapped: {bin(swap_num)}")
        assert swap_num == exp_output


if __name__ == "__main__":
    test_pairwise_swap()
