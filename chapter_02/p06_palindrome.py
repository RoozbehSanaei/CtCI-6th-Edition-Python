import time

from chapter_02.linked_list import LinkedList

'''Palindrome: Implement a function to check if a linked list is a palindrome.


A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. The essential property of a palindrome is its symmetry.

Examples include:

Words: "radar", "level", "civic"
Phrases (ignoring spaces, punctuation, and capitalization): "A man, a plan, a canal, Panama!"
Numbers: 121, 1221, 12321
Palindromes are commonly encountered in wordplay and puzzles, and they also have applications in computer science and mathematics.

'''

def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True

'''
1. Finding the List Center:
  - 'slow' and 'fast' pointers are initialized at the head of the linked list.
  - The fast pointer moves twice as fast as the slow pointer using the "runner" or "tortoise and hare" technique.
  - By the time the fast pointer reaches the end, the slow pointer will be at the middle of the list.

2. Unlink Left and Right Halves:
  - After finding the middle node, 'right_head' points to the first node of the second half.
  - The two halves are unlinked by setting 'slow.next_node' to None.

3. Reverse the Right Half:
  - The function reverses the right half of the list, making two separate half-lists.

4. Iterate and Compare:
  - Using 'left' and 'right' pointers, the function iterates over the two half-lists from the outside inward.
  - It compares their values to check for a palindrome.

5. Undo State Changes:
  - The function reverses the right half-list back to its original state.
  - It then relinks it to the left half-list.

6. Return the Result:
  - Finally, the function returns True if the linked list is a palindrome, otherwise False.

'''
def is_palindrome_constant_space(ll):
    """
    Constant(O(1)) space solution
    """
    # find the list center via the runner technique
    slow = ll.head
    if not slow or not slow.next:
        return True

    fast = slow.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # unlink left and right halves of the list
    right_head = slow.next
    slow.next_node = None
    # reverse the right half of the list
    tail = reverse(right_head)
    # iterate over nodes from the outside in
    left, right = ll.head, tail
    result = True
    while left and right:
        if left.value != right.value:
            result = False
            break
        left = left.next
        right = right.next
    # undo state changes
    reverse(tail)
    slow.next_node = right_head
    return result


def reverse(node):
    """
    reverses a linked list,
    returns the input list's
    tail node as the new head

        Time : O(N)
        Space: O(1)
    """
    previous_node = None
    while node:
        # keep track of the next node
        next_node = node.next
        # point the current node backwards
        node.next = previous_node
        # advance pointers
        previous_node = node
        node = next_node
    return previous_node


def is_palindrome_recursive(ll):
    def get_len(node):
        if not node:
            return 0
        else:
            return 1 + get_len(node.next)

'''
recursive_transverse(node, length): This is the core of the function and it actually performs the palindrome check.

1. if not node or length == 0:
   - Checks if we've reached the end or middle of an even-length list. Returns True and the next node.

2. elif length == 1:
   - Checks if we've reached the middle of an odd-length list. Returns True and skips the middle node.

3. if not _is_palindrome or not fwd_node:
   - Checks if the recursive call found that the list is not a palindrome. Returns False and None if so.

4. if node.value == fwd_node.value:
   - Compares the current node and the symmetric node from the end. If they match, continues; otherwise, returns False.
'''
    def recursive_transverse(node, length):
        if not node or length == 0:  # even list
            return True, node
        elif length == 1:  # odd list
            return True, node.next

        _is_palindrome, fwd_node = recursive_transverse(node.next, length - 2)

        if not _is_palindrome or not fwd_node:
            return False, None

        if node.value == fwd_node.value:
            return True, fwd_node.next
        else:
            return False, None

    return recursive_transverse(ll.head, get_len(ll.head))[0]


test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]

testable_functions = [
    is_palindrome,
    is_palindrome_constant_space,
    is_palindrome_recursive,
]


def test_is_palindrome():
    for f in testable_functions:
        start = time.perf_counter()
        for values, expected in test_cases:
            print(f"{f.__name__}: {values}")
            for _ in range(100):
                assert f(LinkedList(values)) == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    test_is_palindrome()
