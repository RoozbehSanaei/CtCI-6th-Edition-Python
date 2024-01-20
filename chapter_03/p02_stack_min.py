from chapter_03.stack import Stack

'''
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''



'''

The main stack would look like this (from bottom to top): [5, 3, 7, 2, 8]

Now, let's see how self.minvals would evolve:

Push 5: self.minvals becomes [5] (5 is the minimum)
Push 3: self.minvals becomes [5, 3] (3 is the new minimum)
Push 7: self.minvals remains [5, 3] (3 is still the minimum)
Push 2: self.minvals becomes [5, 3, 2] (2 is the new minimum)
Push 8: self.minvals remains [5, 3, 2] (2 is still the minimum)

When you pop values:
If you pop an 8 from the main stack, self.minvals remains [5, 3, 2] because 8 is not the minimum.
If you pop a 2 from the main stack, self.minvals becomes [5, 3], reflecting that the new minimum is 3.
'''

'''
The MinStack class extends a basic stack to efficiently track the minimum element. It uses an auxiliary stack to keep track of minimum values:

    Initialization: Inherits from a base Stack class and initializes an auxiliary stack (self.minvals) for storing minimum values.

    Push Operation: Adds a new element to the stack. If the element is smaller than or equal to the current minimum, it's also pushed onto the minvals stack.

    Pop Operation: Removes the top element from the stack. If this element is the current minimum, it's also removed from the minvals stack.

    Minimum Value Retrieval: Provides the current minimum element by peeking at the top of the minvals stack.
'''

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minvals = Stack()

    def push(self, value):
        super().push(value)
        if not self.minvals or value <= self.minimum():
            self.minvals.push(value)

    def pop(self):
        value = super().pop()
        if value == self.minimum():
            self.minvals.pop()
        return value

    def minimum(self):
        return self.minvals.peek()


def test_min_stack():
    newstack = MinStack()
    assert newstack.minimum() is None

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1


if __name__ == "__main__":
    test_min_stack()
