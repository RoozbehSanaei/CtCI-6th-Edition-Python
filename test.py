from typing import List 
import unittest

class Stack(object):
    def __init__(self):
        self.items = []
    
    def __bool__(self):
        return bool(self.items)

    def peek(self):
        if bool(self):
            return self.items[-1]
        return None
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)


class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def push(self,item: int):
        if not(bool(self)) or (item < self.peek()):
            super().push(item)
        else:
            while (bool(self) and (item > self.peek() )):
                self.temp_stack.push(self.pop())
            
            super().push(item)
            
            while(self.temp_stack):
                super().push(self.temp_stack.pop())


class MinStack(Stack):
    min_vals : Stack
    
    def __init__(self):
        super().__init__()
        self.min_vals = Stack()
    
    def push(self,item):
        if not(self.min_vals) or (item < self.peek()):
            self.min_vals.push(item)
        super().push(item)

    def minimum(self):
        return self.min_vals.peek()
    
    def pop(self):
        value = super().pop()
        if (value == self.minimum()):
            self.min_vals.pop()
        return value

    

class MyQueue(Stack):
    def __init__\



class Tests(unittest.TestCase):
    test_cases = [([1, 2, 3]), ([-1, 0, 1]), (["a", "b", "c", "d", "e", "f"])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                assert len(q) == index
            for index, val in enumerate(sequence, start=1):
                q.remove()
                assert len(q) == len(sequence) - index

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert q.peek() == sequence[0]
            assert len(q) == len(sequence)

    def test_shift_stacks(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert len(q.old_stack) == 0
            assert len(q.new_stack) == len(sequence)
            assert q.new_stack.peek() == sequence[-1]
            q._shift_stacks()
            assert len(q.old_stack) == len(sequence)
            assert len(q.new_stack) == 0
            assert q.old_stack.peek() == sequence[0]

    def test_peek(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
                assert q.peek() == sequence[0]
            q.remove()
            assert q.peek() == sequence[1]

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):  # noqa
                assert q.remove() == sequence[i]

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4
        q.add(101)
        assert q.peek() != 101

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert len(q) == 2
        assert q.remove() == 4
        assert q.remove() == 6
        assert len(q) == 0
        assert not q.remove()



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


class SortedStackTests(unittest.TestCase):
    def test_push_one(self):
        sorted_stack = SortedStack()
        sorted_stack.push(1)
        assert len(sorted_stack) == 1

    def test_push_two(self):
        sorted_stack = SortedStack()
        sorted_stack.push(1)
        sorted_stack.push(2)
        assert len(sorted_stack) == 2

    def test_push_three(self):
        sorted_stack = SortedStack()
        sorted_stack.push(1)
        sorted_stack.push(2)
        sorted_stack.push(3)
        assert len(sorted_stack) == 3

    def test_pop_one(self):
        sorted_stack = SortedStack()
        sorted_stack.push(1)
        assert sorted_stack.pop() == 1

    def test_pop_two(self):
        sorted_stack = SortedStack()
        sorted_stack.push(1)
        sorted_stack.push(2)
        assert sorted_stack.pop() == 1
        assert sorted_stack.pop() == 2

    def test_pop_three(self):
        sorted_stack = SortedStack()
        sorted_stack.push(1)
        sorted_stack.push(2)
        sorted_stack.push(3)
        assert sorted_stack.pop() == 1
        assert sorted_stack.pop() == 2
        assert sorted_stack.pop() == 3

    def test_push_mixed(self):
        sorted_stack = SortedStack()
        sorted_stack.push(3)
        sorted_stack.push(2)
        sorted_stack.push(1)
        sorted_stack.push(4)
        assert sorted_stack.pop() == 1
        assert sorted_stack.pop() == 2
        assert sorted_stack.pop() == 3
        assert sorted_stack.pop() == 4


if __name__ == "__main__":
    test_min_stack()