class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currsum=0
        for n in nums:
            currsum+=n
            maxsum=max(maxsum,currsum)
            if currsum<0:
                currsum=0
            
        return maxsum
## follow up print array as well
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest_total=nums[0]
        highest_seq=[]
        curr_sum=0
        curr_seq=[]
        for n in nums:
            curr_sum+=n
            curr_seq.append(n)
            temp=highest_total
            highest_total=max(highest_total,curr_sum)
            if(highest_total!=temp):
                highest_seq=curr_seq[:]
            if curr_sum<0:
                curr_sum=0
                curr_seq=[]
        print(highest_seq)
        return highest_total

            
        return maxsum
