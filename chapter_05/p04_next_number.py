from typing import Optional

'''
Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
'''

'''
The provided code consists of two functions, _bit and next_smaller, which work together to find the next smaller number 
with the same number of 1 bits in its binary representation as a given number. Here's how the algorithm works in natural language:


Function to Check a Specific Bit
    This function determines if a specific bit (indicated by its position) in a given number is set to 1. It does this by shifting 1 to the left by the position of the bit and then performing a bitwise AND with the given number. If the result is non-zero, it means the bit at that position is 1; otherwise, it's 0.

Function to Find the Next Smaller Number
    Check for Special Case: 
        First, the function checks if the given number is of a form where all bits are 1s (like 111 in binary). For such numbers, there's no smaller number with the same number of 1s, so it returns None.
    
    Count Trailing Ones and Zeros: 
        The function counts the number of consecutive 1s and 0s at the least significant end (rightmost end) of the number's binary representation by:
            Counting how many times the least significant bit is 1 and incrementing a ones counter.
            Once a 0 is encountered, it starts counting how many consecutive zeros follow these ones and increments a zeros counter.
    
    Create the Next Smaller Number: T
        he algorithm then constructs the next smaller number by:
            Turning off (setting to 0) the rightmost 1 that's not part of the trailing ones.
            Turning on (setting to 1) a 0 immediately to the right of this bit.
            This approach retains the same number of 1s but ensures a smaller number by moving a 1 to a less significant position.
    
    Return the Result: 
        The function calculates and returns this new number.
'''
def _bit(x: int, i: int) -> int:
    return x & (1 << i)

def next_smaller(x: int) -> Optional[int]:
    if not x & (x + 1):
        return None
    
    zeros = ones = 0
    
    while _bit(x, i=ones):
        ones += 1
    
    while not _bit(x, i=ones + zeros):
        zeros += 1
    
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
