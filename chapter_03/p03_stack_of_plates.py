import unittest

'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
'''


# Define a Node class to represent an individual element in a stack
'''
The above and below pointers in the Node class serve to connect each node to its adjacent nodes within a stack, forming a doubly-linked list. This makes it easier to navigate and manipulate the stack.
above: Points to the node that is one position above the current node in the stack. If the node is at the top of the stack, above would be None.
below: Points to the node that is one position below the current node in the stack. If the node is at the bottom of the stack, below would be None.
'''



class Node:
    # Node class for representing each element in a stack
    def __init__(self, value):
        self.value = value  # Value of the node
        self.above = None   # Pointer to the node above
        self.below = None   # Pointer to the node below


class Stack:
    # Stack class with a set capacity
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of items in the stack
        self.size = 0             # Current number of items in the stack
        self.top = None           # Top item of the stack
        self.bottom = None        # Bottom item of the stack

    # Check if stack is full
    def is_full(self):
        return self.size == self.capacity

    # Check if stack is empty
    def is_empty(self):
        return self.size == 0

    # Join two nodes within a stack
    def join(self, above, below):
        # Set the pointers between the nodes
        if below:
            below.above = above
        if above:
            above.below = below

    # Add a new item to the top of the stack
    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)

        if self.size == 1:
            self.bottom = n  # If stack was empty, new node is both top and bottom
        self.join(n, self.top)
        self.top = n
        return True

    # Remove and return the top item from the stack
    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    # Remove and return the bottom item from the stack
    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.value


class SetOfStacks:
    # Class to manage multiple stacks, each with a set capacity
    def __init__(self, capacity):
        self.capacity = capacity  # Capacity of each individual stack
        self.stacks = []          # List to hold all the stacks

    # Get the last stack in the list
    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

        # Check if the set of stacks is empty
    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()

    # Add an item to the last stack or to a new stack if the last is full
    def push(self, v):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(v)
        else:
            stack = Stack(self.capacity)
            stack.push(v)
            self.stacks.append(stack)

    # Remove and return the top item from the last stack
    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        v = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return v

    # Remove and return an item from a specific stack
    def pop_at(self, index):
        return self.left_shift(index, True)
    
    '''
    The left_shift method in the SetOfStacks class is used to maintain balance in the stacks after an element is removed from a stack that is not the last one. It works by:

    Removing either the top or bottom element from the specified stack, depending on the remove_top parameter.
    If removing this element empties the stack, the stack is deleted from the set.
    If there's a next stack, the method recursively shifts the bottom element from that next stack to the top of the current stack.

    This process ensures all stacks remain fully utilized, except possibly the last one, after a pop_at operation.
    '''

    # Balance stacks after a pop_at operation
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)
        return removed_item


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        assert lst == list(reversed(range(35)))

    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        assert lst == list(range(4, 35))


if __name__ == "__main__":
    unittest.main()
