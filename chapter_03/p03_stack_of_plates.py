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
class Node:
    def __init__(self, value):
        self.value = value  # The value of the node
        self.above = None  # A reference to the node above this one in the stack
        self.below = None  # A reference to the node below this one in the stack

# Define a Stack class with a maximum capacity
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # The maximum number of elements the stack can hold
        self.size = 0  # The current number of elements in the stack
        self.top = None  # The top element in the stack
        self.bottom = None  # The bottom element in the stack

    # Check if the stack is full
    def is_full(self):
        return self.size == self.capacity

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Join two nodes by setting their above and below pointers
    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    # Push a new value onto the stack
    def push(self, v):
        # If stack is full, cannot push new element
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)  # Create a new node
        # If the stack was empty, this new node becomes the bottom
        if self.size == 1:
            self.bottom = n
        # Connect the new node to the previous top node
        self.join(n, self.top)
        # Update the top pointer to the new node
        self.top = n
        return True

    # Pop the top value off the stack
    def pop(self):
        if not self.top:
            return None
        t = self.top  # Get the current top node
        self.top = self.top.below  # Move the top pointer down
        self.size -= 1  # Decrement the size
        return t.value  # Return the value of the popped node

    # Remove the bottom value from the stack
    def remove_bottom(self):
        b = self.bottom  # Get the current bottom node
        self.bottom = self.bottom.above  # Move the bottom pointer up
        if self.bottom:
            self.bottom.below = None
        self.size -= 1  # Decrement the size
        return b.value  # Return the value of the removed node

# Define a SetOfStacks class that comprises multiple stacks
class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity  # The maximum capacity for each individual stack
        self.stacks = []  # The list holding all individual stacks

    # Get the last stack in the set
    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]  # Return the last stack

    # Check if the set of stacks is empty
    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()

    # Push a new value onto the last stack or a new stack
    def push(self, v):
        last = self.get_last_stack()
        # If there is a last stack and it's not full, push the value
        if last and not last.is_full():
            last.push(v)
        else:
            # Create a new stack and push the value
            stack = Stack(self.capacity)
            stack.push(v)
            self.stacks.append(stack)

    # Pop the top value off the last stack
    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        v = last.pop()
        # If the last stack becomes empty, remove it from the list of stacks
        if last.size == 0:
            del self.stacks[-1]
        return v  # Return the popped value

    # Pop an element from a stack at a specific index
    def pop_at(self, index):
        return self.left_shift(index, True)

    # Shift an element out of a stack to balance it after a pop_at
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]  # Get the stack at the given index
        # Pop the top or bottom element based on remove_top flag
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        # If the stack is empty after removal, delete it
        if stack.is_empty():
            del self.stacks[index]
        # If there are more stacks to the right, shift an element from the next stack
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)  # Push the shifted value to the current stack
        return removed_item  # Return the removed item

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
