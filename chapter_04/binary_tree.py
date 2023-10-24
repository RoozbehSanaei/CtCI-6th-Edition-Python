class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

'''
It creates a new node with the given key using a class specified in self.NodeCls.
If the parent parameter is None, it checks if the tree is empty (self.root is None).
If it is, the new node becomes the root.
If it's not, an exception is raised because the tree already has a root.
If parent is provided, it checks the left and right children.
If the left child is None, it inserts the new node there.
If the right child is None, it inserts the new node there.
If both left and right children exist, an exception is raised because a node can't have more than two children in a binary tree.
'''

    
    def insert(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("a root already exists")

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception("a node cannot have more than two children")
        return new


def example():
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    t.insert(5, n2)
    t.insert(7, n3)
    t.insert(8, n4)

    print(t.root.left.left.left.key)


if __name__ == "__main__":
    example()
