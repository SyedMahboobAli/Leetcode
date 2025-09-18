class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if(n<3):
            return []
        ans=[]
        nums.sort() #because we do low+1 and high-1, if it is sorted it would work
        for i in range(n-2): # even range(n) would work because while (low<high) condition would fail
            if(nums[i]>0): # all positive :no use
                break
            if(i>0 and nums[i]==nums[i-1]): # no duplicate offset
                continue
            low=i+1
            high=n-1
            while(low<high):
                summ=nums[low]+nums[high]+nums[i]
                if(summ==0):
                    ans.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
                    #no break here because there might be more combinations with same offset
                    #2whiles next to avoid duplicates in tuplets
                    while(low<high and nums[low] == nums[low-1]):
                        low+=1
                    while(low<high and nums[high] == nums[high+1]):
                        high-=1
                elif(summ<0):
                    low+=1
                else:
                    high-=1
        return ans 
