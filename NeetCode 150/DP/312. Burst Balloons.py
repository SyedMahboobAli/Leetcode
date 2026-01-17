class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[l][r] represents the maximum coins obtainable by
        # bursting all balloons strictly between indices l and r.
        dp=[[0]*n for _ in range(n)]

        for length in range(2,n):
            for l in range(0,n-length):
                r = l+length
                # STEP 4: Try each balloon k as the LAST balloon burst
                # in the interval (l, r)
                for k in range(l+1,r):
                    #l....k....r
                    # Coins obtained from bursting all balloons
                    # between l and k (exclusive)
                    left_coins = dp[l][k]
                    # Coins obtained from bursting balloon k LAST
                    # At this moment, only l and r are neighbors
                    burst_coins = nums[l]*nums[k]*nums[r]
                    # Coins obtained from bursting all balloons
                    # between k and r (exclusive)
                    right_coins = dp[k][r]

                    dp[l][r] = max(dp[l][r],left_coins + burst_coins + right_coins)
        #between the two virtual balloons
        return dp[0][n-1]
