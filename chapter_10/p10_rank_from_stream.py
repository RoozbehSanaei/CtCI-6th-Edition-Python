'''
Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish to be able
to look up the rank of a numberx (the number of values less than or equal to x). lmplementthe data
structures and algorithms to support these operations. That is, implement the method track ( int
x), which is called when each number is generated, and the method getRankOfNumber(int
x), which returns the number of values less than or equal to x (not including x itself).
EXAMPLE
Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(l) 0
getRankOfNumber(3) = 1
getRankOfNumber(4) 3

'''
'''
    Initialization (__init__):
        When a new node is created, it's initialized with data (if provided). 
        If no data is given, the node is considered empty.
        Each node keeps track of its data, left and right children (initially None), its own count (number of times its data occurs), and the count of nodes in its left subtree.

    Tracking Items (track):
        This method inserts a new item into the BST and updates counts appropriately:
            If the current node is empty, the item becomes the node's data, and its count is set to 1.
            If the item equals the current node's data, the node's count is incremented.
            If the item is smaller than the node's data, it's recursively inserted into the left subtree.
            The left_count of the current node (count of nodes in the left subtree) is also incremented.
            If the item is greater, it's recursively inserted into the right subtree.

    Calculating Rank (get_rank):
        This method calculates the rank of an item in the BST, which is the number of elements less than or equal to the given item:
            If the current node is empty, the rank is 0 (the item is not in the tree).
            If the item matches the current node's data, the rank is the count of the left subtree (left_count).
            If the item is smaller, the rank is found by recursively checking the left subtree.
            If the item is larger, the rank is calculated by adding the left_count, the count of the current node, and the rank obtained recursively from the right subtree.

'''

class RankNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left, self.right = None, None
        self.count = 1 if self.data is not None else 0
        self.left_count = 0

    def track(self, item):
        if self.data is None:
            self.data = item
        elif self.data == item:
            self.count += 1
        elif self.data > item:
            self.left_count += 1
            if self.left:
                self.left.track(item)
            else:
                self.left = RankNode(item)
        else:
            if self.right:
                self.right.track(item)
            else:
                self.right = RankNode(item)

    def get_rank(self, item):
        if self.data is None:
            return 0
        elif self.data == item:
            return self.left_count
        elif self.data > item:
            if self.left:
                return self.left.get_rank(item)
            return 0
        else:
            right_rank = 0 if not self.right else self.right.get_rank(item)
            return self.left_count + self.count + right_rank

# The rest of your code, including the test cases, can remain unchanged.


import unittest

class Test(unittest.TestCase):
  def test_rank_tree(self):
    rt = RankNode()
    self.assertEqual(rt.get_rank(20), 0)
    rt.track(11)
    self.assertEqual(rt.get_rank(20), 1)
    self.assertEqual(rt.get_rank(10), 0)
    rt.track(30)
    rt.track(7)
    rt.track(7)
    rt.track(10)
    rt.track(15)
    rt.track(7)
    rt.track(3)
    rt.track(22)
    self.assertEqual(rt.get_rank(20), 7)
    self.assertEqual(rt.get_rank(7), 1)
    self.assertEqual(rt.get_rank(8), 4)
    self.assertEqual(rt.get_rank(14), 6)

if __name__ == "__main__":
  unittest.main()
