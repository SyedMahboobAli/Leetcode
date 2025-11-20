class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #you can use hashmap used in 2sum, or do binary search the difference and return those indexes or best solution in this case is 2 pointer solution
        l,r=0,len(numbers)-1

        while (l<r):
            curr_sum = numbers[l] + numbers[r]
            if(curr_sum > target):
                r-=1
            elif (curr_sum < target):
                l+=1
            else:
                return (l+1,r+1) #1-indexed
        return []  
