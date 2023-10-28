# Write a method to compute all permutations of a string of unique characters

# Function to generate all permutations of a given string
def get_perms(string):
    permutations = []  # Initialize an empty list to store the permutations
    
    # If the input is None, return None
    if string is None:
        return None
    
    # Base case: if the string is empty, add a space to the permutations list
    if len(string) == 0:
        permutations.append(" ")
        return permutations

    # Recursive case:
    first = string[0]  # Get the first character from the string
    remainder = string[1:]  # Get the string minus its first character
    
    # Recursively get all the permutations of the 'remainder' string
    words = get_perms(remainder)
    
    # Iterate through each word in the list of 'remainder' permutations
    for word in words:
        index = 0  # Initialize index to 0
        # For each character in the word
        for _ in word:
            # Insert the 'first' character at the current index position in the 'word'
            s = insert_char_at(word, first, index)
            # Add this new permutation to our list
            permutations.append(s)
            index += 1  # Move to the next index
    
    return permutations  # Return the final list of permutations

def insert_char_at(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end


# approach 2: Building from permutations of all n-1 character substrings
def get_perms_2(string):
    result = []
    get_perms_inner_2(" ", string, result)
    return result


# Inner function to generate permutations recursively
def get_perms_inner_2(prefix, remainder, result):
    # Base case: if the remainder is empty, a permutation is formed.
    # Append it to the result list.
    if len(remainder) == 0:
        result.append(prefix)

    # Get the length of the remainder string for iteration
    length = len(remainder)
    
    # Loop through each character in the remainder string
    for i in range(length):
        # Slice the string to get the part before the i-th character
        before = remainder[:i]
        
        # Slice the string to get the part after the i-th character
        after = remainder[i + 1:]
        
        # Extract the i-th character
        c = remainder[i]
        
        # Recursive call: Append the i-th character to the prefix and
        # update the remainder by removing the i-th character.
        get_perms_inner_2(prefix + c, before + after, result)



if __name__ == "__main__":
    print(get_perms("str"))
    print(get_perms_2("str"))
