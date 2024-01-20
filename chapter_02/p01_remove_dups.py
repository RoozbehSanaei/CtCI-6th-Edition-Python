import time

from chapter_02.linked_list import LinkedList

'''
The remove_dups function removes duplicate values from a linked list. 
It iterates through the list, using a set to track seen values. 
If a node's value is in the set (a duplicate), it's removed from the list by adjusting the next pointer of the previous node. Otherwise, 
the value is added to the set and the iteration continues. The list's tail is updated at the end, and the modified list is returned with all duplicates removed.

'''


def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll


'''
The remove_dups_followup function removes duplicates from a linked list (ll) using two pointers, 
current and runner, without extra space. It iterates through the list with current, and for each node, 
uses runner to check and remove any subsequent nodes with the same value. After processing all nodes,
 it updates the tail of the list to the last unique node and returns the modified list with duplicates removed. 
 This method is space-efficient but has a higher time complexity due to nested loops.

'''



def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll


testable_functions = (remove_dups, remove_dups_followup)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


def example():
    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)

    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups_followup(ll)
    print(ll)


if __name__ == "__main__":
    example()
