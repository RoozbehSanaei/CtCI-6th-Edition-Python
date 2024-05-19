from chapter_04.binary_search_tree import BinarySearchTree


'''
The code defines a function to find all possible sequences that could have been used to create a given Binary Search Tree (BST). It involves:

    Checking if the BST is empty. If it is, return an empty list.
    A recursive helper function processes each node, generating sequences for left and right subtrees.
    A weave function combines these sequences while maintaining their internal order. This results in all possible sequences that could form the BST when inserted in that order.
'''

def find_bst_sequences(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            sequences = weave(left, right, [node.key], sequences)
    return sequences


'''
The weave function interleaves two lists while maintaining their internal order. Its operation involves the following steps:
    Base Case:
    If one list is empty, the non-empty list is combined with a prefix list and added to a results collection.

    Recursive Call with the Head of the First List:
    The head element of the first list is added to the prefix, and the function is recursively called with the remaining elements of the first list, the entire second list, and the updated prefix.

    Backtracking for the First List: 
        After the recursive call, the last element is removed from the prefix to revert the state.

    Recursive Call with the Head of the Second List:
      The head element of the second list is added to the prefix, and the function is recursively called with the entire first list, the remaining elements of the second list, and the updated prefix.

    Backtracking for the Second List: 
        Similar to the first list, the last element is removed from the prefix for backtracking.

This approach ensures that all possible ways of combining the two lists are explored, respecting their internal ordering.

'''


def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results

'''
The find_bst_sequences_backtracking function generates all possible sequences of node insertions that can create a given Binary Search Tree (BST). It works as follows:

    If the BST is empty (root is null), it returns an empty list.
    A nested backtracking function is defined to build sequences. It takes a list of current node choices and the sequence formed so far.
    The backtracking function iterates through each node in choices, recursively calling itself with updated choices (excluding the current node and including its children if they exist) and an updated sequence including the current node's key.
    When the choices are exhausted, the formed sequence is added to a result list.
    The process starts with the root of the BST and an empty sequence, and the function ultimately returns the list of all possible sequences.

'''


def find_bst_sequences_backtracking(bst):
    if not bst.root:
        return []

    ret_backtracking = []

    def backtracking(choices, weave):
        if not len(choices):
            ret_backtracking.append(weave)
            return

        for i in range(len(choices)):
            nextchoices = choices[:i] + choices[i + 1 :]
            if choices[i].left:
                nextchoices += [choices[i].left]
            if choices[i].right:
                nextchoices += [choices[i].right]
            backtracking(nextchoices, weave + [choices[i].key])

    backtracking([bst.root], [])
    return ret_backtracking


testable_functions = [find_bst_sequences, find_bst_sequences_backtracking]


def test_find_bst_sequences():
    for find_bst in testable_functions:
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        sequences = find_bst(bst)
        assert [2, 1, 3] in sequences
        assert [2, 3, 1] in sequences
        assert len(sequences) == 2


def example():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    # bst.insert(11);
    # bst.insert(14);

    sequences = find_bst_sequences(bst)
    print(sequences)

    sequences = find_bst_sequences_backtracking(bst)
    print(sequences)


if __name__ == "__main__":
    example()
