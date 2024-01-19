# O(N)
import unittest


def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")



class TestUrlify(unittest.TestCase):

    def test_urlify(self):
        test_cases = [
            ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
            ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
            (" a b    ", 4, "%20a%20b"),
            (" a b       ", 5, "%20a%20b%20"),
        ]

        for string, length, expected in test_cases:
            for func in [urlify_algo, urlify_pythonic]:
                with self.subTest(string=string, length=length, func=func.__name__):
                    self.assertEqual(func(string, length), expected)

if __name__ == "__main__":
    unittest.main()