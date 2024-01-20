# O(N)
import unittest


'''
In the context of the string_rotation function, "string rotation" refers to a situation where a string can be formed by 
taking a substring of another string and moving it from one end of this string to the other. 
For example, if you take the string "abcde", a rotation of this string could be "deabc" (where "de" is moved from the end to the beginning).

The function string_rotation checks if one string (s2) is a rotation of another string (s1). 
It does this by concatenating s1 with itself and checking if s2 is a substring of this concatenated string.
 If s2 is found within s1 + s1, then s2 is a rotation of s1.
'''

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
