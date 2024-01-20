# 3.5 Sort Stacks
import unittest

from chapter_03.stack import Stack

'''
Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
'''
class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()


    '''
    The push method in the code is designed to maintain a sorted order in a stack when inserting a new item. 

        Insert if Stack is Empty or Item is Smaller: If the stack is empty or the new item is smaller than the top item of the stack, it's directly pushed onto the stack.

        Reordering for Larger Items:
            If the new item is larger than the top item, the method enters a reordering phase.
            Elements smaller than the new item are temporarily moved to a temp_stack until an appropriate position for the new item is found in the stack.

        Insert New Item: The new item is then pushed onto the stack.

        Restore Elements: Finally, elements from the temp_stack are moved back to the main stack, maintaining the sorted order.

    '''
    def push(self, item):
        if self.is_empty() or item < self.peek():
            super().push(item)
        else:
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())

            super().push(item)

            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())


class Tests(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        assert len(queue) == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert len(queue) == 2

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert len(queue) == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4
