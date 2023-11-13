# Determine if a game of tic-tac-toe is over.
def tic_tac_win(board):
  # Get the size of the board (assuming a square board).
  n = len(board)
  # If the board is empty, return 0 (no winner).
  if n == 0:
    return 0

  # Initialize result trackers for rows, columns, and diagonals.
  row_results  = [0] * n
  col_results  = [0] * n
  diag_results = [0] * 2

  # Iterate over each cell in the board.
  for r in xrange(n):
    for c in xrange(n):
      # Assign a bit mask based on the player occupying the cell.
      if board[r][c] == "o":
        bit_mask = 0b10  # Bit mask for player 'o'.
      elif board[r][c] == "x":
        bit_mask = 0b01  # Bit mask for player 'x'.
      else:
        bit_mask = 0b11  # Bit mask for an empty cell.

      # Update the result trackers with the current cell's bit mask.
      row_results[r] |= bit_mask
      col_results[c] |= bit_mask
      # Update diagonal results if the cell is on a diagonal.
      if r == c:
        diag_results[0] |= bit_mask
      if r == n - c - 1:
        diag_results[1] |= bit_mask

    # Check for a winner in the current row.
    if row_results[r] != 0b11:
      return row_results[r]

  # After checking all rows, check for a winner in columns.
  for c in xrange(n):
    if col_results[c] != 0b11:
      return col_results[c]

  # Finally, check for a winner in diagonals.
  for d in xrange(2):
    if diag_results[d] != 0b11:
      return diag_results[d]

  # If no winner is found, return 0.
  return 0


import unittest

class Test(unittest.TestCase):
  def test_tic_tac_win(self):
    board = [["o", "o", "o"],
             ["x", "x", " "],
             [" ", "x", "x"]]
    self.assertEqual(tic_tac_win(board), 0b10)
    board[0][0] = "x"
    self.assertEqual(tic_tac_win(board), 0b01)
    board[1][1] = "o"
    self.assertEqual(tic_tac_win(board), 0b00)
    board = [["o", "o", "o", "x"],
             ["x", "x", "o", "o"],
             ["x", " ", "x", "x"],
             ["o", "x", "o", "x"]]
    self.assertEqual(tic_tac_win(board), 0b00)
    board[0][3] = "o"
    self.assertEqual(tic_tac_win(board), 0b10)
    board[0][0] = "x"
    self.assertEqual(tic_tac_win(board), 0b01)
    board[2][2] = "o"
    self.assertEqual(tic_tac_win(board), 0b10)

if __name__ == "__main__":
  unittest.main()
