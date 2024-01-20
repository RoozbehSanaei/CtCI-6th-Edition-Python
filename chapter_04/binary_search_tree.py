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
    The insert method in the code is used to insert a new node with a given key into a binary search tree (BST). Here's a brief overview:

        A new node is created with the specified key.

         If the tree is empty (no root), the new node becomes the root.

        The tree is traversed, starting from the root, to find the right position for the new node:
            If the key of the new node is less than the current node's key, the algorithm moves to the left child.
            If the key is greater, it moves to the right child.

            Insertion: 
                The new node is inserted when an empty spot (where a child should be but is None) is found.
                The parent of the new node is set to the current node where it's inserted.

    This method maintains the BST property: left children are less than their parent node, and right children are greater or equal.
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



    '''

    The get_node method searches for and returns a node with a specified key in a binary search tree (BST). 

    Start from Root: 
        The search begins at the root of the BST.

    Traverse Tree: It iteratively traverses the tree:
        If the key matches the current node's key, that node is returned.
        If the key is less than the current node's key, it moves to the left child.
        If the key is greater, it moves to the right child.

    Key Not Found: If the node with the specified key is not found in the tree, an exception is raised indicating no such value exists in the tree.
    '''


    

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
