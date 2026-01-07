class Solution:
    def rob(self, nums: List[int]) -> int:
        def line_rob(nums):
            rob1 , rob2 = 0,0
            for n in nums:
                temp = max(rob2,rob1+n)
                rob1 = rob2
                rob2 = temp
            return rob2
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(line_rob(nums[:-1]),line_rob(nums[1:]))
