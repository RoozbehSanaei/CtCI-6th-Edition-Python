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
class RankNode(object):
    def __init__(self, data=None):
        # Initialize the node with the given data.
        # If the node is created without data, it is considered empty, and 'count' is set to 0.
        # 'left_count' is always initialized to 0.
        self.data = data
        self.left, self.right = None, None
        self.count = 1 if self.data is not None else 0
        self.left_count = 0

  # This method inserts a new integer into the BST and updates the relevant count and left_count values:
  ''' the "current node" starts as the root of the BST when the method is first called, and it changes as the method calls itself
  recursively, traversing down the tree.'''

    def track(self, item):
        # If the current node is empty, set its data to the given item and initialize 'count' to 1.
        if self.data is None:
            self.data = item
        # If the item is equal to the current node's data, increment 'count' by 1.
        elif self.data == item:
            self.count += 1
        # If the item is smaller than the current node's data, update 'left_count' and insert the item in the left subtree.
        elif self.data > item:
            self.left_count += 1
            if self.left:
                self.left.track(item)
            else:
                self.left = RankNode(item)
        # If the item is greater than the current node's data, insert the item in the right subtree.
        else:
            if self.right:
                self.right.track(item)
            else:
                self.right = RankNode(item)

    def get_rank(self, item):
        # If the current node is empty, return 0 (the item is not in the tree).
        if self.data is None:
            return 0
        # If the item is equal to the current node's data, return 'left_count'.
        elif self.data == item:
            return self.left_count
        # If the item is smaller than the current node's data, find its rank in the left subtree.
        elif self.data > item:
            if self.left:
                return self.left.get_rank(item)
            return 0
        # If the item is greater than the current node's data, calculate its rank considering the left subtree and the current node.
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
