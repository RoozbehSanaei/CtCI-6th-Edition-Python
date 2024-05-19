# Determine the number of hits and pseudohits for a guess in Mastermind.
import unittest

def mastermind_hits(code, guess):
    hits = sum(1 for guess_color, code_color in zip(guess, code) if guess_color == code_color)
    hit_colors = {guess_color for guess_color, code_color in zip(guess, code) if guess_color == code_color}
    pseudo_hits = len(set(code) & (set(guess) - hit_colors))
    
    return hits, pseudo_hits



class Test(unittest.TestCase):
  def test_mastermind_hits(self):
    self.assertEqual(mastermind_hits("YYBB", "BBYY"), (0, 2))
    self.assertEqual(mastermind_hits("BYBB", "BBYY"), (1, 1))
    self.assertEqual(mastermind_hits("RGBY", "RGBY"), (4, 0))
    self.assertEqual(mastermind_hits("RGBY", "RBGY"), (2, 2))
    self.assertEqual(mastermind_hits("RGBY", "RRRR"), (1, 0))
    self.assertEqual(mastermind_hits("RRRR", "RBGY"), (1, 0))
    self.assertEqual(mastermind_hits("RRYY", "RYGY"), (2, 0))

if __name__ == "__main__":
  unittest.main()

