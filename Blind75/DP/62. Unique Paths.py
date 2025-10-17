class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # better solution for space using 1D array

        dp=[1]*(n)
        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]
        return dp[-1]

        '''
        At any cell (i, j):

dp[j] holds paths from above (old value before update)

dp[j-1] holds paths from left (just updated)
So we correctly combine both directions, overwriting as we go left→right.
and first is set to 1 anyway, but the first column is always 1 as we second loop we are always starting from index 1
        '''
        #2D dp solution
        dp=[[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1 # base first row and first column has 1 way to reach
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1] #it can come down from dp[i-1][j] to dp[i][j] so all ways to reach that + all ways to reach left cell i.e, dp[i][j-1]
        return dp[m-1][n-1] #return last cell
