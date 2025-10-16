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
