class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #Quickselect, TLE heap is better
        def partition(low,high):
            pivot = nums[high]

            i = low
            for j in range(low,high):
                if nums[j] <= pivot:
                    nums[j],nums[i]= nums[i],nums[j]
                    i += 1
            
            nums[i],nums[high] = nums[high],nums[i]
            return i
        
        low = 0
        high = len(nums) - 1
        target = len(nums) - k

        while(low <= high):
            pivotIndex= partition(low,high)

            if(target == pivotIndex):
                return nums[target]
            elif(pivotIndex < target):
                low = pivotIndex + 1
            else:
                high = pivotIndex -1
        
