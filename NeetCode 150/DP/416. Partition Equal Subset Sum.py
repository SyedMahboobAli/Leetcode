class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #0/1 knapsack problem

        total_sum = sum(nums)
        #base case:
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        dp = [False] *(target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target,num-1,-1): #we are only checking until num
                dp[s] = dp[s] or dp[s-num]

        return dp[target]
