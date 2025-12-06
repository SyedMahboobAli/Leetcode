class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the index of the smalled number
        n=len(nums)
        l,r = 0,n-1
        while (l<r):#for Binary Search we use l<=
            mid = (l+r)//2
            if(nums[mid]>nums[r]):
                l = mid+1 #if mid is greater, it can't be smallest, so l =mid +1
            else:
                r = mid #mid can still be smallest, so r =mid
        min_index = l #though the loop breaks at l =r which is going to be the least

        #define which array target lies to do Binary search.
        # We need to check one more condition if min_index is 0 because if min_index is 0, then min_index - 1 is nums[-1] which would break the logic
        if(min_index == 0):
            l,r = 0,n-1
        elif(nums[0] <= target <=nums[min_index-1]):
            l,r=0,min_index-1
        else:
            l,r=min_index,n - 1
        
        #Finally Binary Search
        while(l<=r):
            mid =(l+r)//2
            if(target == nums[mid]):
                return mid
            elif(target > nums[mid]):
                l = mid+1
            else:
                r = mid-1
        return -1
