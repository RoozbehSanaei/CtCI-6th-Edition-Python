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
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0


    '''
    The join method links two nodes together within a stack. 
    It sets the above pointer of the "below" node to point to the "above" node,
    and the below pointer of the "above" node to point to the "below" node.
    '''

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        
        '''
        If you're adding the first element to an empty stack, 
        that element becomes both the top and the bottom of the stack, so self.bottom is set to n.
        '''
        
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.value


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()

    def push(self, v):
        last = self.get_last_stack()
        if last and not last.is_full():
            last.push(v)
        else:
            stack = Stack(self.capacity)
            stack.push(v)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        v = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return v

    def pop_at(self, index):
        return self.left_shift(index, True)

'''
The left_shift method is used for balancing stacks after a pop_at operation. 
It removes an item from a specific stack at the given index and then shifts items from the next stack to fill in the gap, if needed.
'''
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stacks[index]
# Check if there's another stack to the right of the current one.
        elif len(self.stacks) > index + 1:
            # Remove the bottom item from the next stack to the right.
            v = self.left_shift(index + 1, False)
            # Push that removed item to the top of the current stack.
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
