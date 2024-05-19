from collections import deque

'''
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
'''

'''
Stack Class:

    Initialization: 
        This class represents a stack with a limited size. 
        It uses deque to allow adding and removing elements from both ends.
        
    String Representation: 
        The stack can be converted to a string that shows its elements in stack order (top element first).
    
    Push: 
        Adds a new element to the top of the stack. If the stack is full, it triggers a custom error.
    
    Pop: 
        Removes and returns the top element of the stack. If the stack is empty, it triggers an error.
    
    Top: 
        Retrieves the top element without removing it. If the stack is empty, it triggers an error.

MultiStack Class:
    Initialization: 
        Creates a collection of stacks, each with a specified size.
    
    Get Stack: 
        Retrieves one of the stacks based on its position in the collection.
    
    Push, Pop, Top: 
        These operations are applied to a specific stack within the collection.
    
    String Representation: 
        Provides a textual representation of all the stacks in the collection.

Towers of Hanoi Class:
    Initialization: 
        This class sets up the Towers of Hanoi puzzle using a specific number of disks.
        It organizes these disks on one of the towers in decreasing size, with the largest disk at the bottom and the smallest on top, 
        employing stack push operations to place each disk.

    Solve Method: 
        This method leverages recursion to move disks between the towers following the puzzle's rules. 

    Recursive Solution Method:
        The solution involves recursively moving subsets of disks between the towers. 
        The process uses stack operations, disks are popped from one tower (stack) and pushed onto another. 
        This is done in a specific sequence to ensure compliance with the puzzle's rules:
            Move a smaller subset of disks to a temporary tower (using stack pop from the initial tower and push to the temporary tower).
            Move the largest disk to the target tower (using stack pop from the initial tower and push to the target tower).
            Move the subset of disks from the temporary tower to the target tower (using stack pop from the temporary tower and push to the target tower).

    String Representation: 
        The class provides a method to visualize the current state of the Towers of Hanoi puzzle, showing the arrangement of disks on each tower.

    Accessing Specific Towers: 
        There is functionality to access the state of a specific tower in the puzzle, essentially allowing inspection of the individual stack representing that tower.
'''


# Custom Exceptions
class StackTooBigError(Exception):
    pass


class Stack:
    def __init__(self, stack_size) -> None:
        self.stack_size = stack_size
        self._stack = deque()

    def __str__(self):
        return " ".join(reversed([str(val) for val in self._stack]))

    def push(self, val):
        if len(self._stack) == self.stack_size:
            raise StackTooBigError("stack already reached max size")
        self._stack.append(val)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            raise IndexError("pop attempted from an empty stack")

    def top(self):
        try:
            return self._stack[-1]
        except IndexError:
            raise IndexError("top attempted from an empty stack")


class MultiStack:
    def __init__(self, stack_size, num_stacks=3):
        self.stack_size = stack_size
        self.num_stacks = num_stacks
        self.multistack = [Stack(self.stack_size) for _ in range(self.num_stacks)]

    def get_stack(self, stack_num):
        if 0 > stack_num >= self.num_stacks:
            raise IndexError("stack_num invalid")
        return self.multistack[stack_num]

    def push(self, stack_num, val):
        return self.get_stack(stack_num).push(val)

    def top(self, stack_num):
        return self.get_stack(stack_num).top()

    def pop(self, stack_num):
        return self.get_stack(stack_num).pop()

    def __str__(self):
        str_result = [
            f"Stack {idx}\n{stack}" for idx, stack in enumerate(self.multistack)
        ]
        return "\n".join(str_result)

    def __repr__(self):
        return str(self)


class TowersOfHanoi:
    def __init__(self, stack_size, debug=False):
        self.stack_size = stack_size
        self.debug = debug
        self._stacks = MultiStack(stack_size)
        self.__init_first_stack()

    def __init_first_stack(self):
        for val in range(self.stack_size, 0, -1):
            self._stacks.push(0, val)

    def solve(self):
        if self.debug:
            print(f"Solving Towers of Hanoi - {self.stack_size} size")
        return self.__toh_solve(self.stack_size, 0, 1, 2)

    '''
    First Recursive Call: Move n−1 disks from peg aa to temporary peg bb, using cc as a secondary temporary peg.
    Move Largest Disk: Move the remaining largest disk from aa to cc.
    Second Recursive Call: Move the n−1 disks from temporary peg bb to destination peg cc, using aa as a temporary peg again.
    '''
    
    def __toh_solve(self, n, a, b, c):
        if n > 0:
            self.__toh_solve(n - 1, a, c, b)
            if self.debug:
                print(f"Plate {self._stacks.top(a)} -> Stack {c}")
            self._stacks.push(c, self._stacks.pop(a))
            self.__toh_solve(n - 1, b, a, c)

    def __str__(self):
        return str(self._stacks)

    def get_stack(self, stack_num):
        return self._stacks.get_stack(stack_num)._stack


if __name__ == "__main__":
    for test_case in range(1, 10):
        toh = TowersOfHanoi(test_case, debug=False)
        toh.solve()
        assert toh.get_stack(2) == deque(range(test_case, 0, -1))
        assert toh.get_stack(0) == toh.get_stack(1) == deque()
