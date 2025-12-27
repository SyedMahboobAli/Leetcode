class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Solution model 2: loop. Used in other problems as well
        res = []
        subset = []

        def backtrack(start):
            # Every path is a valid subset
            res.append(subset[:])

            for i in range(start,len(nums)):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return res
        #Solution 1
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            
            #exclude nums[i]
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res
        
