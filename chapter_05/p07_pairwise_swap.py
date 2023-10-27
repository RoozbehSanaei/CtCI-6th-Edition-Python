'''
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''

def pairwise_swap(number):
    # Create a bitmask for all even bits set to 1 (32-bit mask with alternating 1s and 0s)
    # In binary, 0xAAAAAAAA is ...10101010101010101010101010101010
    mask_10 = 0xAAAAAAAA
    
    # Create a bitmask for all odd bits set to 1 (32-bit mask with alternating 0s and 1s)
    # In binary, 0x55555555 is ...01010101010101010101010101010101
    mask_01 = 0x55555555
    
    # AND the number with the even bitmask to zero out all the odd bits
    # This effectively isolates the even bits of the original number
    num_evn = number & mask_10
    
    # AND the number with the odd bitmask to zero out all the even bits
    # This effectively isolates the odd bits of the original number
    num_odd = number & mask_01
    
    # Shift the even bits right by 1 and the odd bits left by 1, and then OR them together
    # This performs the pairwise swap
    swp_num = (num_evn >> 1) | (num_odd << 1)
    
    # Return the resulting swapped number
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
