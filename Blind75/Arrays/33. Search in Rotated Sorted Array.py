#33. Search in Rotated Sorted Array
#approach, find the min index, then there are 2 parts of arrays, both in ascending order, find which part the target lies and set left and right pointer and run standard binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Find the index of the smallest element (pivot)
        l,r=0,len(nums)-1
        while (l<r):
            m=(l+r)//2
            if(nums[m]>nums[r]):
                l=m+1
            else:
                r=m

        min_index=l
# Step 2: Decide which half to search
       
        if (min_index==0):
            l,r=0,len(nums)-1
        elif(nums[0]<=target<=nums[min_index-1]):
            l,r=0,min_index-1
        elif(nums[min_index]<=target<=nums[-1]):
            l,r=min_index,len(nums)-1
# Step 3: Standard binary search
        while (l<=r):
            m=(l+r)//2
            if(nums[m]==target):
                return m
            if(nums[m]<target):
                l=m+1
            else:
                r=m-1
        return -1
