class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1 # base first row and first column has 1 way to reach
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1] #it can come down from dp[i-1][j] to dp[i][j] so all ways to reach that + all ways to reach left cell i.e, dp[i][j-1]
        return dp[m-1][n-1] #return last cell
