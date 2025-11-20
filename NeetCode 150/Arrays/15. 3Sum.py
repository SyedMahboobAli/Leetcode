class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if(n<3):
            return []
        ans = []
        nums.sort()

        for curr_ind in range(n-2):
            if(nums[curr_ind]>0):#all +ve => sum can't be 0
                return ans
            if(curr_ind>0 and nums[curr_ind-1] == nums[curr_ind]):
                continue #first number duplicate handled
            l=curr_ind + 1
            r=n-1
            while(l<r):
                summ=nums[curr_ind]+nums[l]+nums[r]
                if summ==0:
                    #add to the list and move the l,r pointer
                    ans.append([nums[curr_ind],nums[l],nums[r]])
                    l+=1
                    r-=1
                    #below 2 loops to avoid duplicates
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                    while(l<r and nums[r] == nums[r+1]):
                        r-=1
                elif summ>0:
                    r-=1
                else: #summ<0
                    l+=1
        return ans
            
