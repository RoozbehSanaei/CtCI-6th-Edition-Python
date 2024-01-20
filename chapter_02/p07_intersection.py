from chapter_02.linked_list import LinkedList


'''
The intersection function checks if two linked lists intersect and returns the intersecting node:

    Check for Intersection: 
        If the tails of the two lists are different, they don't intersect, and the function returns False.

    Identify Shorter and Longer Lists: 
        Determines which list is shorter and which is longer.

    Align Start Points:
         Advances the start point of the longer list to align it with the shorter list based on their length difference.

    Find Intersection:
        Traverses both lists simultaneously to find the common node where they intersect.

    Return Intersecting Node:
        Returns the node where the intersection occurs, if found.

'''

def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


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