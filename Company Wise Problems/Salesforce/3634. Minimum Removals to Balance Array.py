'''
the array is balanced when max(array) <= k * min(array), and a size-1 array is always balanced. The standard solution is to sort the array, then find the longest contiguous window where nums[r] <= nums[l] * k; the answer is n - longest_window

'''
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        best = 0

        for i, x in enumerate(nums):
            j = bisect_right(nums, x * k)
            best = max(best, j - i)

        return n - best #if window is max, less number of elements are removed

'''
similar 2-pointer solution:
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        best = 0
        r = 0

        for l in range(n):
            while r < n and nums[r] <= nums[l] * k:
                r += 1
            best = max(best, r - l)

        return n - best

'''
