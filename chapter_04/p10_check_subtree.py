from chapter_04.binary_tree import BinaryTree, Node

'''
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
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

'''
The _is_subtree function recursively searches the larger tree to find if a node matches the root of the smaller tree, along with its descendants. 
It first checks if either node is None and returns False if so. Then it checks for a match. If no match is found, 
it continues the search in the left and right children of the current node in the larger tree.
'''

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
