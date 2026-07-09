class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],nums[0] * nums[1] * nums[-1])


'''
The answer is the maximum of these two cases:

The product of the three largest numbers.
The product of the largest number and the two smallest numbers
because two negative numbers can make a large positive product.
'''
