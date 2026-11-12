class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i ,j,k = m-1,n-1,m+n-1

        while(j>=0): #this is important, we need only nums2 to be copied, if we use i here, and i finishes before, nums2 are not copied. If we use j here, nums1 is already in place
            if(i>=0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
