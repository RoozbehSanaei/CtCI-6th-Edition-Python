from chapter_04.binary_tree import BinaryTree

'''
The first_common_ancestor function finds the first common ancestor of two nodes (p and q) in a tree. It works as follows:

    Check for Null: 
        Returns None if either p or q is None.
    Calculate Depths: 
        Uses get_depth to find the depths of p and q.
    Equalize Depths: 
        Moves the deeper node up by the difference in depths.
    Find Common Ancestor: 
        Iteratively moves both nodes up their parent chain until a common node (ancestor) is found.
    Return Result: 
        Returns the common ancestor node.

The get_depth function calculates a node's depth by counting steps from the node to the root.

'''



def first_common_ancestor(p, q):
    if not p or not q:
        return None
    depth_p = get_depth(p)
    depth_q = get_depth(q)
    delta = abs(depth_p - depth_q)
    if depth_p < depth_q:
        for _ in range(delta):
            q = q.parent
    elif depth_q < depth_p:
        for _ in range(delta):
            p = p.parent
    ancestor_p = p
    ancestor_q = q
    while ancestor_p != ancestor_q:
        ancestor_p = ancestor_p.parent
        ancestor_q = ancestor_q.parent
    return ancestor_p


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


if __name__ == "__main__":
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)

    ancestor = first_common_ancestor(n3, n4)
    print(ancestor.key)
