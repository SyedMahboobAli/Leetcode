class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        #quicksort, here the worst case can go to O(n2) so merge sort will be accepted where worst is O(nlogn)
        def quickSort(low,high):
            if low>= high:
                return 
            
            pivotIndex = partition(low,high)

            quickSort(low,pivotIndex -1)
            quickSort(pivotIndex +1,high)
        
        def partition(low,high):
            pivot = nums[high]

            i = low

            for j in range(low,high):
                if(nums[j] <= pivot):
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
            
            nums[i],nums[high] = nums[high],nums[i]

            return i
        
        quickSort(0,len(nums)-1)
        return nums

        #merge sort
        def mergeSort(low,high):
            if low >= high:
                return
            
            mid = low + (high-low) //2
            mergeSort(low,mid)
            mergeSort(mid+1,high)

            merge(low,mid,high)
        
        def merge(low, mid,high):
            temp = []
            i = low
            j = mid+1
            while(i<=mid and j<=high):
                if(nums[i] <= nums[j]):
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while(i<=mid):
                temp.append(nums[i])
                i+=1
            while(j<=high):
                temp.append(nums[j])
                j+=1
            
            nums[low:high+1] = temp

        mergeSort(0,len(nums)-1)     
        return nums       
