from chapter_02.linked_list import LinkedList

'''
fast and slow pointers both start at the head of the linked list (ll.head).
fast moves two steps at a time, while slow moves one step at a time.
If there's a loop, the fast pointer will eventually catch up to the slow pointer, and the while loop will break.
If there's no loop, then fast will reach the end of the list, and the function will return None.
If a loop is detected, a second while loop is used to find the starting node of the loop in the linked list.
If a loop is detected, the slow pointer is reset to the head of the linked list. Both slow and fast pointers then move one node at a time until they meet again. 
When they meet, that node is the starting node of the loop.
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
