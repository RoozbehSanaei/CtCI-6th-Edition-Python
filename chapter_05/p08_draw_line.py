

'''
The draw_line function is designed to draw a horizontal line on a screen represented by a bytearray. 
The screen is a grid of pixels, where each pixel's state (on or off) is represented by a bit within the array. 
The line is specified by its start and end horizontal positions (x1 and x2) and its vertical position (y).
The function modifies the screen array to turn on the bits corresponding to the line. 

    Calculate Byte Positions:
        Determine the byte positions in the array for the start (x1) and end (x2) of the line. 
        This is done by calculating the overall bit position of x1 and x2 on the row y and then dividing by 8 (since there are 8 bits in a byte).

    Create Masks for Start and End Bytes:
        Create a mask for the start byte, which turns on all bits from the x1 position to the end of the byte. 
        This mask is created by shifting a byte filled with 1s to the right by the bit position of x1 within its byte.
        Create a mask for the end byte that turns on all bits up to the x2 position. 
        This mask is formed by shifting a byte filled with 1s to the right by one more than the bit position of x2 and then inverting it.

    Drawing the Line:
        If the start and end of the line are in the same byte, combine the start and end masks with a bitwise AND, then turn on these bits in the screen array.
        If the start and end are in different bytes, perform the following:
            Apply the start mask to the start byte to turn on the bits from x1 to the end of the start byte.
            For each byte between the start and end bytes, turn on all bits by setting the byte value to 0xFF.
            Apply the end mask to the end byte to turn on the bits from the start of the end byte to x2.

    Update the Screen Array:
        Modify the bytes in the screen array as per the above conditions to represent the line on the screen.

'''


def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    left_byte, right_byte = (y * width + x1) // 8, (y * width + x2) // 8
    left_mask, right_mask = 0xFF >> x1 % 8, (0xFF >> x2 % 8 + 1) ^ 0xFF
    if left_byte == right_byte:
        screen[left_byte] |= left_mask & right_mask
    else:
        screen[left_byte] |= left_mask
        for i in range(left_byte + 1, right_byte):
            screen[i] = 0xFF
        screen[right_byte] |= right_mask


def test_0b11111111_0b11111111() -> None:
    screen = bytearray(2)
    draw_line(screen, width=16, x1=0, x2=15, y=0)
    assert screen == bytearray([0b11111111, 0b11111111])


def test_0b01111100() -> None:
    screen = bytearray(1)
    draw_line(screen, width=8, x1=1, x2=5, y=0)
    assert screen == bytearray([0b01111100])


def test_0b01111100_with_y_equals_1() -> None:
    screen = bytearray(3)
    draw_line(screen, width=8, x1=1, x2=5, y=1)
    assert screen == bytearray([0b00000000, 0b01111100, 0b000000000])


def test_0b00000011_0b11111111_0b11000000() -> None:
    screen = bytearray(3)
    draw_line(screen, width=24, x1=6, x2=17, y=0)
    assert screen == bytearray([0b00000011, 0b11111111, 0b11000000])
