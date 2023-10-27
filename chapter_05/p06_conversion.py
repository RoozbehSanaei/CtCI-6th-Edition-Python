'''
Conversion: Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
'''


def bit_swap_required(a: int, b: int) -> int:
    count, c = 0, a ^ b
    while c:
        count, c = count + 1, c & (c - 1)
    return count


def test_29_15() -> None:
    a = 0b11101  # 29
    b = 0b01111  # 15
    assert bit_swap_required(a, b) == 2
