'''
: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

from collections import deque
import random


class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.name)

'''
The create_node_list_by_depth function generates a dictionary mapping each depth level of a binary tree to a linked list of nodes at that level:

    Initialization: 
        It initializes a dictionary levels to hold the linked lists and a queue q for breadth-first traversal. The root node, along with its depth level (0), is added to the queue.

    Breadth-First Traversal: 
        The function enters a loop to process each node in the queue. For each node, it dequeues the node along with its level.

    Level-wise LinkedLists: 
        If the level doesn't exist in levels, a new linked list is created for that level. The node is then added to the linked list corresponding to its level.

    Enqueue Children: 
        The function enqueues the left and right children of the current node (if they exist) into the queue with an incremented level value.

    Return Levels: 
        Once the queue is empty, the function returns the levels dictionary, which contains the nodes of the tree organized by their depth levels. Each level is represented by a linked list of the nodes at that level.
'''


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



def create_node_list_by_depth(tree_root):
    levels = {}
    q = deque()
    q.append((tree_root, 0))
    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            levels[level] = LinkedList()
        levels[level].add(node)
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels

'''

The function create_node_list_by_depth_b(tree) is designed to take a binary tree and create a list of linked lists, where each linked list contains all the nodes at a specific depth level in the tre

    Empty Tree Check: 
        If the tree is empty (None), return an empty list.

    Initialize Variables: 
        Set curr to the tree root, create a result list with a linked list containing the root, and set level to 0.

    Loop Through Levels: 
        Use a while loop to process each tree level until no more nodes are left at the current level.

    Add New Level: 
        Append an empty linked list to result for the next level.

    Process Current Level Nodes: 
        Iterate over nodes in the current level's linked list, adding their left and right children to the next level's linked list.

    Increment Level: 
        Increase level by 1 to move to the next level.

    Return Result: 
        After processing all levels, return the result list, which contains a linked list for each tree level.'''


def create_node_list_by_depth_b(tree):
    if not tree:
        return []

    curr = tree
    result = [LinkedList([curr])]
    level = 0

    while result[level]:
        result.append(LinkedList())
        for linked_list_node in result[level]:
            n = linked_list_node.value
            if n.left:
                result[level + 1].add(n.left)
            if n.right:
                result[level + 1].add(n.right)
        level += 1
    return result

testable_functions = [create_node_list_by_depth, create_node_list_by_depth_b]

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
    levels = create_node_list_by_depth_b(root)
    for level in range(len(levels)):
        print(level,":",str(levels[level]))


if __name__ == "__main__":
    example()
