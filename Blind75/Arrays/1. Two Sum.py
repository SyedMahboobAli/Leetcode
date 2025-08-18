#Brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==target-nums[j]):
                    return [i,j]
        return []

#Two-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in hashmap and hashmap[complement]!= i):
                    return [i,hashmap[complement]]
        return []
#One-pass Hash Table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in hashmap ):
                return [i,hashmap[complement]]
            hashmap[nums[i]]=i   
        return []
