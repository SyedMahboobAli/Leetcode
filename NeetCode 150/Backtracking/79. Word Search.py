class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def backtrack(r,c,idx):
            if idx == len(word):#All characters matched
                return True
            # Boundary + mismatch + visited check should be done here and not in the loop 
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[idx]: 
                return False

            tmp = board[r][c]
            board[r][c]='#'
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r+dr,c+dc
                if backtrack(nr,nc,idx+1):
                    board[r][c] = tmp
                    return True       
            board[r][c] = tmp
            return False

        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False
