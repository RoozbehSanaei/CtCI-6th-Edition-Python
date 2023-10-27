from typing import Optional

'''
Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
'''
def _bit(x: int, i: int) -> int:
    # The expression (1 << i) computes 2^i, effectively setting the i-th bit to 1 and all other bits to 0.
    # The bitwise AND operation (x & (1 << i)) will return a non-zero value if the i-th bit of x is 1,
    # and 0 if the i-th bit of x is 0.
    return x & (1 << i)



def next_smaller(x: int) -> Optional[int]:
    # Check if x is a number like 7 (111 in binary), where all bits are 1s.
    # For such numbers, a smaller number with the same number of 1s doesn't exist.
    if not x & (x + 1):
        return None
    
    # Initialize counters for the number of consecutive 1s (ones)
    # and zeros (zeros) in the least significant bits of x.
    zeros = ones = 0
    
    # Count the number of trailing 1s in x's binary representation.
    while _bit(x, i=ones):
        ones += 1
    
    # Count the number of trailing zeros following the trailing 1s.
    while not _bit(x, i=ones + zeros):
        zeros += 1
    
    ''' The idea is to take the rightmost 1 that's not part of the trailing 1s and switch it off (make it 0). 
    Then, immediately to its right, switch on a 0 (make it 1). This retains the same number of 1s but creates a 
    smaller number because you've moved a 1 to a less significant bit.
    '''
    return x - (1 << ones) - (1 << zeros - 1) + 1



def next_larger(x: int) -> int:
    zeros = ones = 0
    while not _bit(x, i=zeros):
        zeros += 1
    while _bit(x, i=zeros + ones):
        ones += 1
    
    return x + (1 << zeros) + (1 << ones - 1) - 1


def test_next_smaller_than_0b11111() -> None:
    assert next_smaller(0b11111) is None


def test_next_smaller_than_0b10110() -> None:
    assert next_smaller(0b10110) == 0b10101


def test_next_larger_than_0b10110() -> None:
    assert next_larger(0b10110) == 0b11001


if __name__ == "__main__":
    x = int(input("Enter a positive integer: "))
    while x < 0:
        x = int(input(str(x) + " is not positive. Please try again: "))
    print("Next smaller: ", next_smaller(x))
    print("Next larger: ", next_larger(x))
