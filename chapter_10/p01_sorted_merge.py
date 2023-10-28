'''
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
'''

def sorted_merge(a, b):
    # Initialize index to point to the last element of array 'a'
    index = len(a) - 1
    
    # Initialize index_b to point to the last element of array 'b'
    index_b = len(b) - 1
    
    # Initialize index_a to point to the last "real" element in 'a' (ignoring extra spaces)
    index_a = len(a) - len(b) - 1

    # Loop runs until all elements of 'b' are considered
    while index_b >= 0:
        
        # Check if the current element at index_a in 'a' is greater than the current element at index_b in 'b'
        if index_a >= 0 and a[index_a] > b[index_b]:
            
            # If so, place this element from 'a' into the sorted position (pointed by 'index') in 'a'
            a[index] = a[index_a]
            
            # Decrement index_a to move to the next largest element in 'a'
            index_a -= 1
        else:
            # Place the current element from 'b' into the sorted position (pointed by 'index') in 'a'
            a[index] = b[index_b]
            
            # Decrement index_b to move to the next largest element in 'b'
            index_b -= 1
        
        # Decrement index to move to the next largest sorted position in 'a' (if index > 0)
        if index > 0:
            index -= 1
    
    # Return the sorted, merged array
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
