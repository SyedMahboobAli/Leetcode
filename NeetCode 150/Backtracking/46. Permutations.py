class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False for _ in range(len(nums))] # tracks which elements are already used

        def backtrack():
            if len(nums) == len(subset):
                res.append(subset[:])
                return
            # Try every number as the next choice
            for i in range(len(nums)):
                if used[i]: # skip if number already used
                    continue
                used[i] = True
                subset.append(nums[i])
                backtrack()
                subset.pop()
                used[i] = False
        
        backtrack()
        return res
