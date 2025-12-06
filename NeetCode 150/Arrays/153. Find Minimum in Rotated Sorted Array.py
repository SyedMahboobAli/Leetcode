class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1 
        while (l<r): #for Binary Search we use l<=
            mid = (l+r) // 2
            if(nums[mid] > nums[r]): 
                l = mid+1 #if mid is greater, it can't be smallest, so l =mid +1
            else:
                r = mid #mid can still be smallest, so r =mid
        return nums[l] #though the loop breaks at l =r which is going to be the least, we can also use r
