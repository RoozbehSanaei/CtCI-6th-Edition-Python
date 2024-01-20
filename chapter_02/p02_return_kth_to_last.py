from chapter_02.linked_list import LinkedList

'''
The kth_to_last function finds the k-th last element in a linked list. 
It uses two pointers: leader advances through the list, while follower starts moving after leader is k steps ahead. 
When leader reaches the end, follower is at the k-th last element. The function then returns this element.
'''

def kth_to_last(ll, k):
    leader = follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    return follower

'''
The kth_last_recursive function finds the k-th last element in a linked list using recursion:

    Initialization: It sets up a counter and starts from the head of the list.

    Helper Function: This recursive function traverses the list. When it reaches the end (head is None), it starts incrementing counter on the way back up the recursion.

    Count and Identify: As the recursion unwinds, when counter matches k, the function identifies the k-th last element and returns it.

    Result: The main function initiates this process with helper(head, k) and returns the k-th last element found. The approach uses O(N) space due to recursion.
'''



# O(N) space
def kth_last_recursive(ll, k):
    head = ll.head
    counter = 0

    def helper(head, k):
        nonlocal counter
        if not head:
            return None
        helper_node = helper(head.next, k)
        counter = counter + 1
        if counter == k:
            return head
        return helper_node

    return helper(head, k)


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
