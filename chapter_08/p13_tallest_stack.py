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


'''
    Main Function - tallest_stack:
        Purpose: 
            Determines the tallest stack possible with a given set of boxes.
        Process:
            Sorting: 
                The boxes are sorted in descending order based on a specific dimension (height, width, or depth).
            Iterative Calculation: 
                The function iterates through each box, treating each as the potential base of a stack, and computes the tallest stack that can be formed with that box at the bottom.
            Finding Maximum Height: 
                It keeps track of and updates the maximum height of all possible stacks.

    Nested Recursive Function - tallest_for_bottom:
        Purpose: 
            Calculates the height of the tallest stack possible with a given starting box.
        Process:
            Base Case: 
                If all boxes have been considered (indicated by reaching the end of the list), the function calculates and returns the total height of the current stack.
            Recursive Step: 
                For each box, the function checks if it can be stacked on the current stack (the new box must be smaller in all dimensions than the box it's being placed on).
                
                Stacking and Recursion: 
                    If the box can be stacked, it's added to the current stack, and the function recursively calls itself with the updated stack and the next box in line.
                Skipping a Box: 
                    If the box cannot be stacked, the function moves to the next box without adding it to the stack, again calling itself recursively.
                Backtracking: 
                    After exploring each possibility (stacking or not stacking a box), the function backtracks to explore other stacking combinations with different boxes.

    Returning the Tallest Stack Height:
        Final Output: 
            After iterating through each box as a potential base and computing the tallest stack for each, the main function returns the maximum height obtained from all these combinations.
'''

def tallest_stack(boxes):
    boxes.sort(reverse=True)

    def tallest_for_bottom(cur_stack, cur_box_idx):
        if cur_box_idx == len(boxes):
            return reduce(lambda x, y: x + y.height, cur_stack, 0)

        if (
            cur_stack[-1].height > boxes[cur_box_idx].height
            and cur_stack[-1].width > boxes[cur_box_idx].width
            and cur_stack[-1].depth > boxes[cur_box_idx].depth
        ):
            return tallest_for_bottom(cur_stack + [boxes[cur_box_idx]], cur_box_idx + 1)

        return tallest_for_bottom(cur_stack, cur_box_idx + 1)

    largest_height = 0
    for i, box in enumerate(boxes):
        largest_height = max(largest_height, tallest_for_bottom([box], i + 1))
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
