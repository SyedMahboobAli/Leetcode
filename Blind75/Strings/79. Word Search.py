class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #backtracking using Hashset solution
        n,m=len(board), len(board[0])

        path=set()# to track visited cells

        def dfs(r,c,i):
            # Base case: all letters matched
            if(i==len(word)):
                return True
            # Out of bounds or mismatch or already visited
            if(r<0 or c<0 or r>=n or c>=m or word[i] !=board[r][c] or (r,c) in path):
                return False
            # Mark current cell as visited
            path.add((r,c))
            # Explore 4 directions
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            # Backtrack (unmark current cell)
            path.remove((r,c))

            return res
# Try starting from every cell
        for i in range(n):
            for j in range(m):
                if(dfs(i,j,0)):
                    return True
        return False


'''
approach 2: Backtracking (Visited Array)
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
in dfs func:  
visited[r][c] = True
res = ...         
visited[r][c] = False
return res

approach 3: Backtracking (Optimal), no extra space, BEST
board[r][c] = '#'
res = ...
board[r][c] = word[i]
return res

'''
