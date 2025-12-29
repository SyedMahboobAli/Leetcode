class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # Board representation
        board = [["."] * n for _ in range(n)]

        # Track columns and diagonals already occupied (Is Safe)
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            # If all rows are filled, store the solution
            if row == n:
                res.append(["".join(r) for r in board])

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Check column and diagonals
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Place queen
                backtrack(row + 1)

                # Backtrack (remove queen)
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res
