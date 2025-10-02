class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #solution 1 best
        dp=[float('inf')] * (amount+1)
        dp[0]=0 # if base case not mentioned,  all dp values will be inf only
        for coin in coins:
            for i in range(coin,amount+1):#check notes for why coin
                dp[i]=min(dp[i],1+dp[i-coin])
        return dp[amount] if dp[amount] != float('inf') else -1
