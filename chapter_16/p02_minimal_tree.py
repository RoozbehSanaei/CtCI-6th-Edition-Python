from typing import Optional, List

'''
Minimal Tree: 
Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
'''

class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item


    '''
    The disp function is designed to visually display the structure of a binary tree:

        Indentation: It uses the nesting parameter to determine the level of indentation for each node, creating a visual hierarchy.

        Output Current Node: It starts by adding the current node's value (self.val) to the output.

        Left Subtree: If the left child (self.left) exists, it recursively calls disp on the left child, increasing the nesting level for indentation, and prefixes it with "L:" to indicate a left branch.

        Right Subtree: Similarly, if the right child (self.right) exists, it does the same as for the left child, but with a prefix "R:" to indicate a right branch.

        Return Output: The function returns the string output, which contains the formatted representation of the tree.
    '''
        
    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.val}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()


'''
The array_to_binary_tree function converts a sorted array into a balanced binary tree:

    If start index is greater than end, it returns None, indicating no node to create in this segment.

    Calculates the middle index of the current segment of the array to create a balanced tree.

    Uses the middle element of the array to create the root node of the current subtree.

    Recursive Construction:
        Recursively builds the left subtree using the left half of the current segment.
        Recursively builds the right subtree using the right half.

    Returns the root node of the constructed binary tree.

The result is a balanced binary tree constructed from the sorted array.

'''

def array_to_binary_tree(arr: List[int], start: int, end: int) -> Optional[Node]:
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = Node(arr[mid])
    root.left = array_to_binary_tree(arr, start, mid - 1)
    root.right = array_to_binary_tree(arr, mid + 1, end)
    
    return root

if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    print(array_to_binary_tree(test_array, 0, len(test_array) - 1))
