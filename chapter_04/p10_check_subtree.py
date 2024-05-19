from chapter_04.binary_tree import BinaryTree, Node

'''
The code defines a custom node class for a binary tree, where each node can be compared to another node. 
The comparison checks if both nodes have the same value and their respective left and right child nodes are also equal.

Additionally, there's a custom binary tree class using these specialized nodes.

The main functionality includes a method to determine if one binary tree is a subtree of another. 
It checks if the structure and values of the second tree (the potential subtree) completely match a part of the first tree. 
This method first ensures both trees are valid (not empty) and then uses a recursive helper method to perform the comparison.

The recursive helper method checks each node in the first tree to see if it matches the root of the second tree.
 If it finds a match, it further checks if the entire structure beneath that node matches the second tree, 
 confirming it as a subtree. If not, it recursively checks the same for each child node of the current node in the first tree.

'''

class ComparableTreeNode(Node):
    def __eq__(self, other):
        if not isinstance(other, ComparableTreeNode):
            return False
        return (
            self.key == other.key
            and self.left == other.left
            and self.right == other.right
        )


class ComparableBinaryTree(BinaryTree):
    NodeCls = ComparableTreeNode


# "needle in a haystack"
# haystack == the thing we're searching inside
# needle == the thing we're looking for
def is_subtree(haystack_tree, needle_tree):
    if not haystack_tree or not needle_tree:
        return False
    return _is_subtree(haystack_tree.root, needle_tree.root)



def _is_subtree(haystack_node, needle_node):
    if haystack_node is None or needle_node is None:
        return False
    if haystack_node == needle_node:
        return True

    return _is_subtree(haystack_node.left, needle_node) or _is_subtree(
        haystack_node.right, needle_node
    )


if __name__ == "__main__":
    t1 = ComparableBinaryTree()
    n1 = t1.insert(1, None)
    n2 = t1.insert(2, n1)
    n3 = t1.insert(3, n1)
    n4 = t1.insert(4, n2)
    n5 = t1.insert(5, n2)
    n7 = t1.insert(7, n3)
    n8 = t1.insert(8, n4)

    t2 = ComparableBinaryTree()
    n40 = t2.insert(4, None)
    n80 = t2.insert(8, n40)
    # n90 = t2.insert(9, n40)

    print(is_subtree(t1, t2))
