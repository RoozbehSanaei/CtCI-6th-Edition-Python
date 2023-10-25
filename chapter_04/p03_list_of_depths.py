from collections import deque

from chapter_02.linked_list import LinkedList


class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

'''
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

from collections import deque

def create_node_list_by_depth(tree_root):
    # Initialize an empty dictionary to hold the linked lists for each depth.
    levels = {}
    
    # Initialize a deque for Breadth-First Search (BFS).
    q = deque()
    
    # Start with the root node at level 0.
    q.append((tree_root, 0))

    # Loop until the deque is empty.
    while len(q) > 0:
        # Dequeue a node and its level.
        node, level = q.popleft()
        
        # If this level is not in 'levels' yet, add it.
        if level not in levels:
            levels[level] = LinkedList()
        
        # Add the dequeued node to the linked list for its level.
        levels[level].add(node)

        # Enqueue the left child with incremented level if it exists.
        if node.left:
            q.append((node.left, level + 1))
        
        # Enqueue the right child with incremented level if it exists.
        if node.right:
            q.append((node.right, level + 1))
    
    # Return the dictionary with levels as keys and linked lists of nodes as values.
    return levels


def create_node_list_by_depth_b(tree):
    # If the tree is empty, return an empty list.
    if not tree:
        return []
    
    # Initialize 'curr' to point to the root of the tree.
    curr = tree
    
    # Initialize 'result' as a list of a single linked list containing the root node.
    result = [LinkedList([curr])]
    
    # Initialize 'level' to keep track of the current depth.
    level = 0

    # Loop as long as the linked list at the current level is not empty.
    while result[level]:
        # Append an empty linked list for the next level.
        result.append(LinkedList())
        
        # Iterate over each node in the linked list at the current level.
        for linked_list_node in result[level]:
            # Retrieve the actual tree node from the linked list node.
            n = linked_list_node.value
            
            # If the left child exists, add it to the linked list for the next level.
            if n.left:
                result[level + 1].add(n.left)
            
            # If the right child exists, add it to the linked list for the next level.
            if n.right:
                result[level + 1].add(n.right)
        
        # Increment 'level' to move on to the next depth.
        level += 1
    
    # Return the list of linked lists.
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

    levels = create_node_list_by_depth(root)
    print(levels)


if __name__ == "__main__":
    example()
