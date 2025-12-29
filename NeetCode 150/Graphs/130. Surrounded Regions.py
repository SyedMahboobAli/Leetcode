class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #similar to atlantic/pacific. All O's that are connected and connected to border can't be changed to X. So reverse the approach and start from boundaries to solve the problem
        if not board or not board[0]:
            return
        
        rows,cols = len(board), len(board[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!="O":
                return
            
            board[r][c] = "T"  # mark as safe
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
        # Run DFS from border 'O's
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][cols-1] == 'O':
                dfs(i,cols-1)
        
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[rows-1][j] =='O':
                dfs(rows-1,j)
        # Flip the board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] ='X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        
        
