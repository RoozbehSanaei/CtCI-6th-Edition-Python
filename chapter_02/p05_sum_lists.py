import pytest

from chapter_02.linked_list import LinkedList

'''
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
'''

'''
The sum_lists function adds two numbers represented as linked lists (ll_a and ll_b), 
with each node containing a single digit and the least significant digit at the head of the list. 
It iterates through both lists, summing corresponding digits. For each sum, it calculates the "digit part," 
which is the sum modulo 10 (the rightmost digit), and the "carry part," which is the sum divided by 10 (the carry-over value for the next pair of digits). 
The "digit part" is added to a new list, while the "carry part" is carried over to the next iteration.
After processing all digits, any remaining carry is added to the list. The function then returns this new list, representing the total sum.
'''


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = NumericLinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll

'''
The sum_lists_recursive function adds two numbers represented by linked lists and returns the sum as a new linked list, using a recursive approach:

    Base Case: When both lists are fully traversed, any remaining carry is added to the sum list, and the sum list is returned.

    Recursive Summing and Carrying:
        If one list is longer, the function adds the value from the remaining list and any carry to the sum list.
        If both lists have nodes, their values and any carry are added.
        In both scenarios, the sum's digit part is stored in the sum list, and any excess is carried over.
        The process continues recursively with the next nodes.

    Returning the Result: The recursion continues until all nodes in both lists are processed, resulting in a sum list representing the total sum.
'''

def sum_lists_recursive(ll_a, ll_b) -> "NumericLinkedList":
    def sum_lists_helper(ll1_head, ll2_head, remainder, summed_list):
        if ll1_head is None and ll2_head is None:
            if remainder != 0:
                summed_list.add(remainder)
            return summed_list
        elif ll1_head is None:
            result = ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head, ll2_head.next, result // 10, summed_list)
        elif ll2_head is None:
            result = ll1_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head.next, ll2_head, result // 10, summed_list)
        else:
            result = ll1_head.value + ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(
                ll1_head.next, ll2_head.next, result // 10, summed_list
            )

    return sum_lists_helper(ll_a.head, ll_b.head, 0, NumericLinkedList())


class NumericLinkedList(LinkedList):
    def __init__(self, values=None):
        """handle integer as input"""
        if isinstance(values, int):
            values = [int(c) for c in str(values)]
            values.reverse()
        elif isinstance(values, list):
            values = values.copy()

        super().__init__(values)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10**place
        return number


def test_numeric_linked_list():
    ll = NumericLinkedList(321)
    assert ll.numeric_value() == 321
    assert ll.values() == [1, 2, 3]


testable_functions = (sum_lists, sum_lists_recursive)


@pytest.fixture(params=testable_functions)
def linked_list_summing_function(request):
    return request.param


test_cases = (
    # inputs can either be list of integer or integers
    # a, b, expected_sum
    pytest.param([1], [2], [3], id="single_digit"),
    pytest.param([0], [0], [0], id="single_digit_zero"),
    pytest.param([], [], [], id="empty"),
    pytest.param([7, 1, 6], [5, 9, 2], [2, 1, 9], id="3-digit equal length A"),
    pytest.param([3, 2, 1], [3, 2, 1], [6, 4, 2], id="3-digit equal length B"),
    pytest.param(123, 1, [4, 2, 1], id="3-digit and single digit"),
    pytest.param([9, 9, 9], [1], [0, 0, 0, 1], id="carry end"),
    pytest.param([9, 9, 9], [9, 9, 9], [8, 9, 9, 1], id="multiple carry"),
)


@pytest.mark.parametrize("a, b, expected", test_cases)
def test_linked_list_addition(linked_list_summing_function, a, b, expected):
    ll_a = NumericLinkedList(a)
    ll_b = NumericLinkedList(b)
    ll_result = linked_list_summing_function(ll_a, ll_b)
    assert ll_result.values() == expected
    assert (
        ll_a.numeric_value() + ll_b.numeric_value()
        == NumericLinkedList(expected).numeric_value()
    )

    ll_result_reverse = linked_list_summing_function(ll_b, ll_a)
    assert ll_result_reverse.values() == expected


def example():
    ll_a = LinkedList.generate(4, 0, 9)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))


if __name__ == "__main__":
    example()
    pytest.main(args=[__file__])
