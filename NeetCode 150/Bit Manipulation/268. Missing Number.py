class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res^i^nums[i]
        res = res^(i+1) #to complete the range, i would be len(nums) -1
        return res
