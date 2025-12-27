class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #subset 1 has unique elements. Here we have duplicate elements
        nums.sort() # Sort to group duplicates together
        res = []
        subset = []

        def backtrack(start):
            # Every path is a valid subset
            res.append(subset[:])

            for i in range(start,len(nums)):
                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()

        backtrack(0)
        return res
