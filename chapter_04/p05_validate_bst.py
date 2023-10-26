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
The algorithm uses a recursive approach to traverse the tree and check these properties. It does so by keeping track of the minimum (min_val) and maximum (max_val) allowable values for each node as it traverses down the tree.

When going left, the max_val is updated to the current node's value.
When going right, the min_val is updated to the current node's value.
By doing this, it checks not just local conditions (i.e., comparing a node with its immediate children) but also more global conditions that consider ancestors and descendants, which is crucial for validating a BST.
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
