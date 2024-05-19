# Write a method to compute all permutations of a string of unique characters


'''
    Initialize Permutations List: 
        Start by creating an empty list where all the permutations will be stored.

    Handle None String: 
        If the input string is None, the function returns None, as permutations can't be generated for a non-existent string.

    Base Case for Empty String: 
        If the input string is empty, add an empty space to the permutations list. 
        This is the base case for the recursion.

    Recursive Case:
        Extract the first character of the string. This character will be inserted into different positions in the permutations of the remaining string.
        Get the remainder of the string by removing the first character.

    Generate Permutations of the Remainder: 
        Call the same function recursively to get all permutations of the remainder of the string.

    Insert the First Character in Each Position:
        For each permutation of the remainder, insert the first character at every possible position within the permutation. 
        For instance, if the first character is 'A' and one of the permutations of the remainder is 'BC', you insert 'A' at three positions, resulting in 'ABC', 'BAC', and 'BCA'.
        Use a helper function to insert the character at the desired position.

    Return All Permutations: 
        After iterating through all permutations of the remainder and inserting the first character at all possible positions, return the final list of permutations.
'''
def get_perms(string):
    permutations = []
    if string is None:
        return None
    if len(string) == 0:
        permutations.append(" ")
        return permutations
    first = string[0]
    remainder = string[1:]
    words = get_perms(remainder)
    for word in words:
        index = 0
        for _ in word:
            s = insert_char_at(word, first, index)
            permutations.append(s)
            index += 1
    return permutations

def insert_char_at(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end



'''
    Starting the Process:
        Begin with a function designed to generate permutations of a given string.
        This function starts by creating an empty list where the permutations will be stored.
        It then calls a helper function, initially providing it with a blank starting point, the original string, and the empty list for storing permutations.

    Generating Permutations (Helper Function):
        The helper function is where the permutations are actually created. 
        It uses a recursive approach, meaning it repeatedly calls itself with different inputs until a certain condition is met.
        
        Initially, the function checks if the string to permute is empty. 
        If it is, this indicates that a complete permutation has been formed, which is then added to the list of permutations.
        If the string is not empty, the function proceeds to iterate through each character in the string.
            For each character, the function divides the string into two parts: the part before the current character and the part after.
            It then takes the current character and adds it to an ongoing combination (which started as blank).
            The function calls itself again, but now with a new combination (the ongoing combination plus the current character) and a new string to permute (composed of the parts of the string before and after the current character, effectively excluding the current character).
        This recursive process continues, gradually building up combinations and storing each complete permutation in the list, until all possible permutations are generated.

'''
def get_perms_2(string):
    result = []
    get_perms_inner_2(" ", string, result)
    return result

def get_perms_inner_2(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1:]
        c = remainder[i]
        get_perms_inner_2(prefix + c, before + after, result)




if __name__ == "__main__":
    print(get_perms("str"))
    print(get_perms_2("str"))
