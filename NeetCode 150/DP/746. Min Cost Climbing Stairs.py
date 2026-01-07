class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #sol2:space optimized
        prev1 = prev2 = 0
        for i in range(2,len(cost)+1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = curr
        return prev1
        #Sol1: dp array
        n= len(cost)
        dp = [0]* (n+1) #note dp[0] and dp[1] are 0 as we haven't yet stepped on any stair
        for i in range(2,n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
