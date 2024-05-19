import random
from collections import defaultdict

'''
    Binary Search Tree Components:

        Node Structure:
            Holds an individual element's value.
            Links to:
                A parent element.
                Two child elements (left and right).
            Manages subtree size, representing the count of elements in its subtree.

        Binary Search Tree (BST) Structure:
            Initializes without any elements.
            Supports operations like:
                Inserting elements.
                Deleting elements.
                Finding specific elements.
                Randomly selecting elements.

    Operations:

        Adding Elements:
            Inserts a new element based on BST rules.
            Traverses the tree to find the correct position.
            Updates subtree sizes during the insertion process.

        Deletion:
            Locate the Node to Delete:
                Start at the tree's root and search for the node with the target value, similar to the search algorithm.
            If the node is not found, the process ends.

            Node Deletion Cases:
                Node with No Children (Leaf Node): Simply remove the node.
                Node with One Child: Remove the node and link its child directly to the node's parent.
            Node with Two Children: Find the node with the smallest value in the right subtree (often called the successor). Replace the value of the node to be deleted with the successor's value. Then, delete the successor node, which will have at most one child.

            Update Subtree Sizes:
                After deletion, update the size of each ancestor node to ensure accurate subtree size information. This is done while backtracking from the deletion point to the root.


    Finding Specific Nodes in the Binary Search Tree:
        Start at the tree's root.
        Compare the target value with the current node's value.
        If the target is less, move to the left child; if greater, to the right child.
        Repeat the process until the target value is found or a leaf node is reached.
        If found, return the node; if not, indicate the value is not in the tree.

    Random Node Selection in the Binary Search Tree

        Starting at the tree's root.
        At each node, choose among three actions: return the current node, move to the left child, or move to the right child.
        Make this choice based on weighted probabilities, where the weights are derived from the sizes of the left and right subtrees and the current node (considered as 1).
        Continue the process until a node is selected.

    Auxiliary Functions:
        Finding the Smallest Element in a Subtree:
            Aids in the deletion process.
            Locates and returns the smallest element in a specified subtree.
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.size = 1

    @property
    def left_size(self):
        if self.left:
            return self.left.size
        return 0

    @property
    def right_size(self):
        if self.right:
            return self.right.size
        return 0


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            current.size += 1
            if current.key >= key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    def delete_helper(self, node, key):

        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_helper(node.left, key)

        elif key > node.key:
            node.right = self.delete_helper(node.right, key)

        else:
            if node.left is None:
                temp, node = node.right, None
                return temp

            elif node.right is None:
                temp, node = node.left, None
                return temp

            temp = min_val_node(node.right)
            node.key = temp.key
            node.right = self.delete_helper(node.right, temp.key)

        node.size -= 1
        return node

    def delete(self, key):
        self.delete_helper(self.root, key)

    def get_node(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current

            if current.key > key:
                current = current.left
            else:
                current = current.right
        raise Exception("No such value in the tree")

    def get_random_node(self):
        current = self.root
        # with probability 1/N = 1/(1+l+r) return node
        # with probability l/N go down left
        # with probability r/N go down right

        while current:
            choices = ["self", "left", "right"]
            choice_weights = [1, current.left_size, current.right_size]
            decision = random.choices(choices, choice_weights)[0]

            if decision == "self":
                return current

            if decision == "left":
                current = current.left
            elif decision == "right":
                current = current.right
            else:
                raise RuntimeError("Should not be possible")


def min_val_node(node):
    current = node
    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


def example():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)
    bst.delete(12)

    chosen_counts = defaultdict(int)
    for _ in range(6000):
        node = bst.get_random_node()
        chosen_counts[node.key] += 1

    print(chosen_counts.values())


if __name__ == "__main__":
    example()
