class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[[]]* (target+1)
        dp[0]=[[]]
        candidates.sort()
        for c in candidates:
            for t in range(c,target+1):
                for comb in dp[t-c]:
                    new_comb=comb+[c]
                     # Add c to previous combination
                    dp[t].append(new_comb)
        return dp[target]
'''
This is throwing error. Memory Limit Exceeded. this is similar to coin change solution. If you need count, you can use it or use backtracking pick/don't pick solution.

Count combinations	DP
Print all combinations	✅ Backtracking (LeetCode #39)
Each number used once (no repeats)	Backtracking + skip duplicates (LeetCode #40)
'''

# Backtracking Solution
#  ✅ Recommended approach
class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
        res=[]
        path=[]
        def backtrack(start,target,path): #start imp because we don't want to check all again, only indexes ahead
            # Base Case: if target is zero, we found a valid combination
            if(target==0):
                res.append(path.copy()) #or path[:]
                return 
            # Explore from current index onwards
            for i in range(start, len(candidates)):
                if(candidates[i]>target):
                    continue # you can sort the candidates and use break instead
                #choose the number
                path.append(candidates[i])
                # Since we can reuse same number, pass i instead of i+1
                backtrack(i,target-candidates[i],path)
                # Backtrack
                path.pop()
        
        backtrack(0,target,[])
        return res
        '''
another approach  
        class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, target, path):
            # Base Case: if target is zero, we found a valid combination
            if target == 0:
                res.append(path[:])
                return
            # Explore from current index onwards
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                # Choose the number
                path.append(candidates[i])
                # Since we can reuse same number, pass i instead of i+1
                backtrack(i, target - candidates[i], path)
                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return res
       '''
       
