class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],1+dp[i-coin]) #i is the amount we are trying to make
        return dp[amount] if dp[amount] != float('inf') else -1
