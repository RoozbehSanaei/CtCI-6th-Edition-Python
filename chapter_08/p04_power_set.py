import copy

'''
Power Set: Write a method to return all subsets of a set.
'''

'''
    Start with the Entire Set:
        Begin with a given set and start from the last element. 
        If the set is empty, the only subset is the empty set.

    Recursive Approach:
        To find all subsets of the set, first find all subsets of the set excluding the last element. 
        This is done by calling the same process on the smaller set (excluding the last element).

    Creating New Subsets:
        For each subset found in the previous step, create new subsets by adding the last element of the original set to each of them.

    Combining Old and New Subsets:
        Combine the subsets found in the previous step (which don't include the last element) with the new subsets (which include the last element).

    Repeat for Each Element:
        Repeat this process for every element in the set, moving from the last element towards the first. 
        In each step, the subsets are expanded by considering the inclusion and exclusion of the current element.

    Result:
        Once all elements have been considered, the result is a collection of all possible subsets of the original set, including the empty set and the set itself.

'''


# Solution using recursion
def get_subsets_a(setz, index=None):
    if index is None:
        index = len(setz) - 1
    if index == -1:
        return [[]]

    old_subs = get_subsets_a(setz, index - 1)
    new_subs = []
    item = setz[index]
    '''
    The loop iterates over all existing subsets, appending both the original subset and a new subset that includes the current item, 
    '''
    for val in old_subs:
        new_subs.append(val) # Append the old_subs
        entry = copy.deepcopy(val)  # Create a deep copy to avoid altering the original subset
        entry.append(item)  # Add the new element to this copy
        new_subs.append(entry)  # Append the new subset


    return new_subs

'''
    Initialize a Collection for All Subsets:
        Start by creating an empty collection to hold all the subsets.

    Determine the Total Number of Subsets:
        Calculate the total number of possible subsets. This is found by taking 2 to the power of the number of elements in the set. 
        Each element can either be in or out of a subset, hence 2 choices per element.

    Iterate Over All Subset Possibilities:
        For each number from 0 to one less than the total number of subsets, interpret this number as a binary representation of a subset. 
        In this binary number, each bit represents whether the corresponding element in the set is included in the subset.

    Convert Each Number to a Subset:
        For each number, convert it into a subset. 
        Start with an empty subset, and for each bit in the number, if the bit is 1, include the corresponding element from the set in the subset.

    Check Each Bit of the Number:
        Go through the bits of the number from least significant to most significant.
        If a bit is set (i.e., it's 1), include the element from the set that corresponds to this bit's position.

    Build the Subset:
        For each bit that is set in the number, add the corresponding element from the original set to the current subset.

    Store the Subset:
        Add the created subset to the collection of all subsets.

    Complete Process for All Numbers:
        Repeat this process for each number in the range. Once complete, the collection will contain all possible subsets of the original set.

'''


# Combinatorics Solution
def get_subsets_b(aset):
    all_subsets = []
    max_n = 1 << len(aset)
    for k in range(max_n):
        subset = convert_int_to_set(k, aset)
        all_subsets.append(subset)
    return all_subsets

def convert_int_to_set(x, aset):
    subset = []
    index = 0
    k = x  
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:  # Check if the least-significant bit is 1 and the element is not in 'subset'
            subset.append(aset[index])  # Append the corresponding element from 'aset' to 'subset'
        index += 1  
        k >>= 1  # Right-shift 'k' to check the next bit
    return subset

'''
    Initialize a List of Subsets:
        Start with a list that already contains the empty subset. 
        This is because the empty subset is always a part of the power set (the set of all subsets) of any set.

    Define a Recursive Function:
        Create a recursive function that takes two parameters:
            the current subset being built and the remaining elements of the original set that haven't been considered yet.

        Base Case for Recursion:
            The recursion stops (base case) when there are no more elements left to consider for inclusion in the current subset.

    Iterate Through Remaining Elements:
        For each element in the remaining elements:
            First, check if adding this element to the current subset creates a subset that hasn’t been included in the list of subsets yet.
            If it’s a new subset, add it to the list of subsets.
            Then, recursively call the function with two updates:
                The current subset now includes the element just considered.
                The remaining elements exclude this element and all elements before it. This prevents considering subsets that have already been formed.

    Start the Recursive Process:
        Begin the recursive process with an empty current subset and the original set as the remaining elements.

    Complete and Return All Subsets:
        Once the recursive process is complete, return the list of all subsets.


'''

# alternative recursive solution.
def get_subsets_c(_set):
    subsets = [[]]

    def recurse(current_set, remaining_set):
        if len(remaining_set) == 0:  # base case
            return

        for i in range(len(remaining_set)):
            if current_set + [remaining_set[i]] not in subsets:
                subsets.append(current_set + [remaining_set[i]])
                recurse(current_set + [remaining_set[i]], remaining_set[i + 1 :])

    recurse([], _set)
    return subsets


testable_functions = [get_subsets_a, get_subsets_b, get_subsets_c]

test_cases = [({1, 2, 3}, {(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)})]


def test_get_subsets():
    for input_set, expected in test_cases:
        for get_subsets in testable_functions:
            results = get_subsets(list(input_set))
            results = {tuple(s) for s in results}
            assert results == expected


if __name__ == "__main__":
    print(get_subsets_a([1, 2, 3]))
    print("")
    print(get_subsets_b([1, 2, 3]))
    print("")
    print(get_subsets_c([1, 2, 3]))
