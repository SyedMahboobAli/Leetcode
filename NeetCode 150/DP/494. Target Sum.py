class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #1D DP solutin
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        P = (total+target) // 2
        
        dp = [0]*(P+1)
        dp[0] = 1

        for num in nums:
            for s in range(P,num-1,-1):
                dp[s] += dp[s-num]
        
        return dp[P]
        #2D dp solution
        total = sum(nums)
        n = len(nums)

        if abs(target) > total:
            return 0
        
        dp = [[0]*(2*total + 1) for _ in range(n+1)]
        dp[0][total] = 1 #base case

        for i in range(1,n+1):
            num = nums[i-1]
            for s in range(2*total+1):
                if dp[i-1][s] != 0:
                    dp[i][s-num] += dp[i-1][s]
                    dp[i][s+num] += dp[i-1][s]
        return dp[n][total+target]
