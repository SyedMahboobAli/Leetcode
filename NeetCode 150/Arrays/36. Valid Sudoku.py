class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for r in range(9):
            for c in range (9):
                if(board[r][c] == '.'):
                    continue
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].add(board[r][c])
                if board[r][c] in column[c]:
                    return False
                else:
                    column[c].add(board[r][c])
                
                grid_index=(r//3)*3 + (c//3)
                if board[r][c] in grid[grid_index]:
                    return False
                else:
                    grid[grid_index].add(board[r][c])
        return True
