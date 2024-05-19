'''
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
'''

'''
The key trick is that the merging process starts from the end of each array and works its way to the beginning. 
This allows the algorithm to take advantage of the sorted nature of the arrays, 
so it can place the largest elements at the end first and proceed in descending order. 
This ensures that smaller elements don't overwrite larger ones as the algorithm progresses.
'''

'''
The sorted_merge algorithm is designed to merge two sorted lists into a single sorted list.

    Prepare for Merging:
        You have two lists. The first one has extra space at its end, just enough to accommodate all elements of the second list.

    Start from the End:
        Begin at the end of both lists. The idea is to fill the extra space in the first list by comparing elements from both lists, starting from their ends.

    Compare and Place:
        Compare the last elements of both lists.
        If the last element of the first list (ignoring the extra space) is larger than the last element of the second list, 
        place this larger element in the last available space of the first list.
        Otherwise, place the last element of the second list in this space.

    Move Backwards Through Lists:
        After placing an element, move backwards in the list from which the element was taken.
        Continue the comparison and placement, moving backwards through both lists.

    Repeat Until Done:
        Keep repeating this process. Each time, either the last considered element of the first list or the second list is placed into the correct position in the extra space of the first list.

    Finish with a Merged List:
        The process continues until all elements of the second list are placed. This results in the first list containing all elements from both lists, now sorted.

'''

def sorted_merge(a, b):
    index = len(a) - 1
    index_b = len(b) - 1
    index_a = len(a) - len(b) - 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index] = a[index_a]
            index_a -= 1
        else:
            a[index] = b[index_b]
            index_b -= 1
        if index > 0:
            index -= 1
    return a



def fill_array_up_to(maxnum):
    return [2 * i + 4 for i in range(maxnum)]


def fill_array_with_buffer(length, buffer):
    return [3 * i + 1 for i in range(length)] + ([0] * buffer)


def test_sorted_merge():
    a = [9, 10, 11, 12, 13, 0, 0, 0, 0]
    b = [4, 5, 6, 7]
    expected = [4, 5, 6, 7, 9, 10, 11, 12, 13]
    assert sorted_merge(a, b) == expected


def example():
    a = fill_array_with_buffer(5, 10)
    b = fill_array_up_to(10)
    print(a, b)
    print(sorted_merge(a, b))


if __name__ == "__main__":
    example()
