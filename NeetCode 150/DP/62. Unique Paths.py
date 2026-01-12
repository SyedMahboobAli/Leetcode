class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #1D DP solution
        dp= [1] *(n)
        for i in range(1,m): #1,m is imp as dp is initialized with 1 and dp[-1] will fetch wrong val. In 2D it is initialized with 0 so np
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
        #2D DP solution
        dp = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 1 #Base Case
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
