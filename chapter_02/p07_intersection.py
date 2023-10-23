from chapter_02.linked_list import LinkedList


# Check if the tail nodes of list1 and list2 are the same.
    # If they are not, then the lists do not intersect.
    if list1.tail is not list2.tail:
        return False

    # Determine which list is shorter and which is longer.
    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    # Calculate the difference in lengths between the two lists.
    diff = len(longer) - len(shorter)

    # Initialize nodes for traversal.
    shorter_node, longer_node = shorter.head, longer.head

    # Advance the node in the longer list by the calculated difference.
    # This ensures that shorter_node and longer_node will meet at the intersection point.
    for _ in range(diff):
        longer_node = longer_node.next

    # Traverse the lists simultaneously until the nodes meet, which is the intersection point.
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail

    # should be 1
    assert intersection(a, b).value == 1
