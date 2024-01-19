import time
import unittest

'''
The compress_string function compresses a given string by counting consecutive occurrences of each character and forming a new string that consists of each character followed by its count.
 This is achieved by iterating over the string, keeping track of the count of repeated characters, and updating the compressed version accordingly. 

The last character and its count are appended to compressed. 
This is necessary because the loop's condition only checks for changes between consecutive characters,
so the last sequence is not handled within the loop.
The function then returns the shorter of the original string and the compressed string. 
This is achieved by joining the compressed list into a string and using min with key=len to compare the lengths.
'''


def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
