class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Sol 2: Binery Search + greedy
        tails = []

        for num in nums:
            idx = bisect.bisect_left(tails,num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        
        return len(tails)

        #Sol 1: DP O(n2) not optimal
        n = len(nums)
        dp = [1] * n # every element itself is an LIS of length 1

        for i in range(n):
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

