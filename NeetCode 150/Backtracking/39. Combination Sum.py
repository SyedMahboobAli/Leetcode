class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        #we are sending start to avoid duplicate combination. For array [2,3] and target 5 , [2,3] & [3,2] are both same order mismatch is allowed. If we check one number along with its duplicates, we have already checked all possible combinations using that number, so we can move ahead now and check all possible combinations without that number.
        def backtrack(start,total):
            if total == 0:
                res.append(subset.copy())

            for i in range(start,len(candidates)):
                if candidates[i] > total:
                    continue #if sorted you can break altogether since all ahead are greater
                subset.append(candidates[i])
                backtrack(i,total - candidates[i]) #since duplicates are allowed
                subset.pop()

        backtrack(0,target)    
        return res

        
