class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #0^a= a
        #a^a = 0
        res = 0
        for num in nums:
            res ^= num
        return res
