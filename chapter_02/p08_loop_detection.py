from chapter_02.linked_list import LinkedList

'''
Fast and Slow Pointers: Uses two pointers, fast moving two steps and slow one step, to check for a cycle. If they meet, a loop exists.

No Loop Found: If fast or fast.next is None, the list has no loop, and the function returns None.

Locate Loop Start: Resets slow to the head and moves both slow and fast one step at a time until they meet again, indicating the start of the loop.

Return Loop Start: Returns the node where fast and slow meet, marking the beginning of the loop.
'''

def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected
