'''

💡 Key Insight (Optimized O(1))
Instead of checking the whole board every move:
Track row counts, column counts
Track diagonal and anti-diagonal
Player 1 → +1
Player 2 → -1
If any count reaches ±n, that player wins.
'''
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antiDiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val

        if row == col:
            self.diag += val

        if row + col == self.n - 1:
            self.antiDiag += val

        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diag) == self.n or
            abs(self.antiDiag) == self.n):
            return player

        return 0
