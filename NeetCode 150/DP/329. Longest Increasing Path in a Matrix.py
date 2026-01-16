class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m,n=len(matrix),len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        directions =[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if dp[r][c] !=0:
                return dp[r][c]
            
            best = 1 #path legth atleast 1 that is cell itself

            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best,1+dfs(nr,nc))

            dp[r][c] =best
            return best
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
        
        return ans
