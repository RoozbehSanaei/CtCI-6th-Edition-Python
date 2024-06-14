'''
: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

from collections import deque
import random

class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def values(self):
        return [x.value for x in self]

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))



class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.name)



def create_node_list_by_depth(tree_root):
    levels = {}
    queue = deque()
    queue.append((tree_root,0))
    while queue:
        node, level = queue.pop()
        if level not in levels:
            levels[level] = LinkedList()
        levels[level].add(node)
        if node.right:
            queue.append((node.right, level+1))
        if node.left:
            queue.append((node.left, level+1))
    return levels





def create_node_list_by_depth(tree_root):
    level = 0
    levels = [LinkedList([tree_root])]

    while levels[level]:
        levels.append(LinkedList())
        for node in levels[level]:
            n = node.value
            if n.right:
                levels[level+1].add(n.right)
            if n.left:
                levels[level+1].add(n.left)
        level += 1
    return levels





testable_functions = [create_node_list_by_depth]

def test_create_node_list_by_depth():
    for f in testable_functions:
        node_h = BinaryNode("H")
        node_g = BinaryNode("G")
        node_f = BinaryNode("F")
        node_e = BinaryNode("E", node_g)
        node_d = BinaryNode("D", node_h)
        node_c = BinaryNode("C", None, node_f)
        node_b = BinaryNode("B", node_d, node_e)
        node_a = BinaryNode("A", node_b, node_c)
        lists = f(node_a)
        assert lists[0].values() == LinkedList([node_a]).values()
        assert lists[1].values() == LinkedList([node_b, node_c]).values()
        assert lists[2].values() == LinkedList([node_d, node_e, node_f]).values()
        assert lists[3].values() == LinkedList([node_h, node_g]).values()

def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)
    levels = create_node_list_by_depth(root)
    for level in range(len(levels)):
        print(level,":",str(levels[level]))

if __name__ == "__main__":
    example()
