class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #sol2 X0R : 0^1^2^3 ^ 0^1^3 = (0^0)^(1^1)^(3^3)^2 = 0^0^0^2 = 2
        #n^n=0, 0^n=n
        res=0
        for i in range(len(nums)):
            res=res^i^nums[i]
        res^=len(nums) #to complete the range
        return res
        
        #sol 1 simple math
        expected_sum=0
        for i in range(len(nums)+1):
            expected_sum+=i
        actual_sum=0
        for i in nums:
            actual_sum+=i
        return expected_sum-actual_sum
