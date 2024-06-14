'''
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
'''

from chapter_04.binary_search_tree import BinarySearchTree




'''
The in_order_successor function determines the in-order successor of a given node in a binary search tree:

    Null Check: If the input node is None, return None.

    Right Child Present: If the input node has a right child, find the leftmost node in the right subtree.

    No Right Child: If no right child, move up the tree using parent pointers.
        Continue moving up as long as the current node is a right child of its parent.

    Return Ancestor: Return the ancestor node where the current node is a left child. If no such ancestor exists (the input node is the rightmost node), return None.
'''

def in_order_successor(input_node):
    if input_node is None:
        return None

    if input_node.right:
        current = input_node.right
        while current.left:
            current = current.left
        return current

    ancestor = input_node.parent
    child = input_node
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor


def test_in_order_successor():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = in_order_successor(test)
        if succ is not None:
            assert succ.key == y
        else:
            assert succ == y


if __name__ == "__main__":
    test_in_order_successor()
