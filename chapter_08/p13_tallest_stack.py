import unittest
from functools import reduce



'''
Stack of Boxes: You have a stack of n boxes, with widths wi
, heights hi
, and depths di
. The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
'''


# Define the function tallest_stack which takes a list of boxes as an argument
def tallest_stack(boxes):
    # Sort the boxes in descending order
    boxes.sort(reverse=True)

    # Define a nested function tallest_for_bottom
    # to find the tallest stack starting with a specific bottom box
    def tallest_for_bottom(cur_stack, cur_box_idx):
        # Base case: if we've gone through all the boxes,
        # return the total height of the current stack
        if cur_box_idx == len(boxes):
            return reduce(lambda x, y: x + y.height, cur_stack, 0)

        # Check if the current box can be stacked on top of the stack's last box
        if (
            cur_stack[-1].height > boxes[cur_box_idx].height
            and cur_stack[-1].width > boxes[cur_box_idx].width
            and cur_stack[-1].depth > boxes[cur_box_idx].depth
        ):
            # If yes, add the box to the stack and move to the next box
            return tallest_for_bottom(cur_stack + [boxes[cur_box_idx]], cur_box_idx + 1)

        # If not, just move to the next box without adding it to the stack
        return tallest_for_bottom(cur_stack, cur_box_idx + 1)

    # Initialize the variable to store the height of the tallest stack
    largest_height = 0
    # Loop through each box and use it as the bottom of a potential stack
    for i, box in enumerate(boxes):
        # Find the tallest stack using the current box as the bottom
        # and update the largest_height if needed
        largest_height = max(largest_height, tallest_for_bottom([box], i + 1))
    # Return the height of the tallest stack found
    return largest_height



class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height


def test_null():
    assert tallest_stack([]) == 0


def test_single_box():
    assert tallest_stack([Box(3, 2, 1)]) == 3


def test_two_conflicting_boxes():
    assert tallest_stack([Box(3, 2, 1), Box(5, 4, 1)]) == 5


def test_two_stackable_boxes():
    assert tallest_stack([Box(3, 2, 1), Box(6, 5, 4)]) == 9


if __name__ == "__main__":
    unittest.main()
