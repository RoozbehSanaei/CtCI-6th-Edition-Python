class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
'''
a Python method for inserting a new node with a given key into a binary search tree (BST). Here's a quick rundown of what it does:

First, it creates a new node with the given key.
If the tree is empty (self.root is None), it sets the root of the tree to the new node.
If the tree isn't empty, it starts from the root and traverses the tree :
    If key is smaller than the current node's key, it goes left.
    If key is greater or equal, it goes right.
    When it finds a None spot (either current.left or current.right), it inserts the new node there and sets the parent link.
'''
    def insert(self, key):
        new = Node(key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            if current.key > key:
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


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)
