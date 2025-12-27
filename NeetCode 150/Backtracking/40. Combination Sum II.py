class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort() # Sort to handle duplicates and pruning

        def backtrack(start,target):
            if target == 0:
                res.append(subset[:])
                return
            for i in range(start,len(candidates)):
                # Prune search if current number exceeds remaining target.
                #All numbers ahead are more than target
                if candidates[i] > target:
                    break
                
                # Skip duplicates at the same recursion level
                # i > start ensures we only skip duplicates in the same depth
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                subset.pop()

        backtrack(0,target)
        return res
        
