'''
Write a method to compute all permutations of a string whose charac-
ters are not necessarily unique. The list of permutations should not have duplicates.
'''


'''
    Initiating the Permutation Process:
        The process starts with a function that aims to generate permutations of a given string.
        Inside this function, an empty list is created to store the permutations.
        A frequency table is built for the string, which counts the occurrences of each character in the string.
        Then, a helper function is called with the frequency table, an initially empty string (which will serve as a prefix), 
        the length of the original string, and the empty list for permutations.

    Building a Frequency Table:
        A separate function is used to create a frequency table for the string.
        It iterates through each character in the string.
        For each character, if it's not already in the frequency table, it's added with a count of zero.
        The count for each character is then incremented accordingly.
        The function returns this frequency table.

    Generating Permutations (Helper Function):
        The helper function is where the permutations are generated.
        It first checks if the number of characters remaining to be added to the permutation is zero. If so, a complete permutation has been formed, which is then added to the list of permutations.
        If there are still characters to be added, the function iterates through each character in the frequency table.
        For each character with a non-zero count in the frequency table:
            The count of that character is decreased by one (to account for its usage in the current permutation).
            The helper function is recursively called with an updated prefix (the current prefix plus the character), the reduced count of remaining characters, and the same frequency table (with the updated count of the current character).
            After the recursive call, the count of the character in the frequency table is reset to its original value. This step ensures that the character count is correct for the next iteration.

'''

def print_perms(string):
    result = []
    letter_count_map = build_freq_table(string)
    perms_inner(letter_count_map, "", len(string), result)
    return result


# returns dictionary <string, integer>
def build_freq_table(string):
    letter_count_map = {}
    for letter in string:
        if letter not in letter_count_map:
            letter_count_map[letter] = 0
        letter_count_map[letter] += 1
    return letter_count_map


def perms_inner(letter_count_map, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return
    for character in letter_count_map:
        count = letter_count_map[character]
        if count > 0:
            letter_count_map[character] -= 1
            perms_inner(
                letter_count_map, prefix + character, remaining - 1, result
            )
            letter_count_map[character] = count


if __name__ == "__main__":
    print(print_perms("aaf"))
