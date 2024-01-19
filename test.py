# O(N)
import unittest


def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    char_list2 = list(string)

    new_index = len(char_list)-1

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list2[new_index - 2 : new_index+1] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list2[new_index] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list2[new_index+1:])



class TestUrlify(unittest.TestCase):

    def test_urlify(self):
        test_cases = [
            ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
            (" a b    ", 4, "%20a%20b"),
            ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
            (" a b       ", 5, "%20a%20b%20"),
        ]

        for string, length, expected in test_cases:
            self.assertEqual(urlify_algo(string, length), expected)

if __name__ == "__main__":
    unittest.main()