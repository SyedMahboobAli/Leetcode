class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #in coin change 1 we want min, here we need total count of combinations
        dp = [0] * (amount+1) #different to coin change 1
        dp[0] = 1 #different to coin change 1

        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] += dp[x-coin]
        return dp[amount]
