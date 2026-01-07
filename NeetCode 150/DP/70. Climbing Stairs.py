class Solution:
    def climbStairs(self, n: int) -> int:
        #solution 2 space optimized 
        cur, prev=1,1
        for _ in range(2,n+1):
            prev,cur=cur,cur+prev
        return cur
        # Solution 1: array
        dp = [0] * (n+1)
        dp[0] = 1 #Base case
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

