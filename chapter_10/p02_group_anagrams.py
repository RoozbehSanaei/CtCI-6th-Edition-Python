from collections import defaultdict

'''
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.
'''
'''
The group_anagrams function is an algorithm designed to group words that are anagrams of each other. Here's a description of how it works, using natural language and avoiding specific variable names:

    Setting Up a Collection:
        The algorithm begins by preparing a way to collect groups of words. Each group will consist of words that are anagrams of each other.

    Processing Each Word:
        For every word in the provided list of words, the algorithm performs a couple of steps:
            First, it rearranges the letters of the word in alphabetical order and converts them to lowercase. This step is crucial as it provides a standard form to identify anagrams. For instance, 'Listen' and 'Silent' both would transform to 'eilnst'.
            Then, it groups the original word with other words that have the same sorted letter combination. So, all words that transform into 'eilnst' would be grouped together.

    Gathering Groups of Anagrams:
        After all words are processed, the algorithm goes through each group of anagrams.
        It compiles these groups into a new list. Each group of anagrams, now in the form of a list, is added to this new list.

    Result:
        The final output is a list where words are grouped together with their anagrams. Each group of anagrams is adjacent in this list, though the groups themselves may not be in any specific order.
'''

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        anagrams[sorted_word].append(word)

    sorted_words = []
    for similar_words in anagrams.values():
        sorted_words.extend(similar_words)
    return sorted_words


def test_group_anagrams():
    words = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]
    expected_sort = [
        "abed",
        "bead",
        "bade",
        "later",
        "alert",
        "alter",
        "altered",
        "alerted",
    ]
    assert group_anagrams(words) == expected_sort


def example():
    words = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]
    print(group_anagrams(words))


if __name__ == "__main__":
    example()
