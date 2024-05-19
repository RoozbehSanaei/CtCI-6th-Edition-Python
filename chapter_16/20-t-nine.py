# Determine which words match a sequence of T9 key presses.
''' T9: On old cell phones, users typed on a numeric keypad and the phone would provide a list of words 
that matched these numbers. Each digit mapped to a set of O - 4 letters. Implement an algorithm 
to return a list of matching words, given a sequence of digits. You are provided a list of valid words 
(provided in whatever data structure you'd like). The mapping is shown in the diagram below:'''
 
LETTERS = {0: [], 1: [], 2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'],
  5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'],
  8: ['t','u','v'], 9: ['w','x','y','z']}

PREFIX_TREE = {'a':{'b':{'':True,'a':{'c':{'u':{'s':{'':True}}}}}},
               't':{'r':{'e':{'e':{'':True}}}},
               'u':{'s':{'':True,'e':{'':True,'d':{'':True},
                                      'r':{'':True},'s':{'':True}}}},
               'z':{'o':{'o':{'':True,'m':{'':True}}}}}
                                                
def t9_words(digits):
  if len(digits) == 0:
    return []
  partials = [('', PREFIX_TREE)]
  for digit in digits:
    next_partials = []
    for partial, node in partials:
      for letter in LETTERS[int(digit)]:
        if letter in node:
          next_partials.append((partial + letter, node[letter]))
    partials = next_partials
  words = []
  for word, node in partials:
    if '' in node:
      words.append(word)
  return words

import unittest

class Test(unittest.TestCase):
  def test_t9_words(self):
    digits = "222287"
    self.assertEqual(t9_words(digits), ['abacus'])
    digits = "8733"
    self.assertEqual(t9_words(digits), ['tree', 'used'])

if __name__ == "__main__":
  unittest.main()

