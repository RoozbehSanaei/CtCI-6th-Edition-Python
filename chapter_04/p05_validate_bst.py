from chapter_04.binary_search_tree import BinarySearchTree
from chapter_04.binary_tree import BinaryTree

'''
Validate BST: Implement a function to check if a binary tree is a binary search tree.
Specifically, for a binary tree to be a BST:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''

def is_binary_search_tree(tree):
    return _is_bst(tree.root)


'''
The _is_bst function checks if a binary tree is a binary search tree (BST). It recursively verifies two conditions for each node:

    The node's value must be greater than a given minimum (min_val) and less than a given maximum (max_val).
    These conditions must hold true for both the left and right subtrees.

If a node violates these conditions or if a node is absent (indicating a leaf), the function returns False or True respectively. 
The function updates min_val and max_val as it traverses down the tree to maintain the BST property: left child values are less than the parent, and right child values are greater.
'''

def _is_bst(node, min_val=None, max_val=None):
    if not node:
        return True
    if (min_val and node.key < min_val) or (max_val and node.key >= max_val):
        return False
    return _is_bst(node.left, min_val, node.key) and _is_bst(
        node.right, node.key, max_val
    )


def test_is_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    t = BinaryTree()
    n1 = t.insert(5, None)
    n2 = t.insert(4, n1)
    n3 = t.insert(6, n1)
    n4 = t.insert(3, n2)
    t.insert(6, n2)
    t.insert(5, n3)
    t.insert(2, n4)

    assert not is_binary_search_tree(t)
    assert is_binary_search_tree(bst)
