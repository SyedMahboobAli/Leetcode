class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        word_set = set(wordDict)  # Faster lookups
        dp=[False]* (n+1)
        
        dp[0]=True # base case

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]=True
                    break # No need to check further
        return dp[n]

'''
s = "applepenapple"
wordDict = ["apple", "pen"]
dp[0]=true # base case
dp[5] = True because "apple" is in the dict.

dp[8] = True because "pen" is in the dict and dp[5] was True.

dp[13] = True because "apple" again and dp[8] was True.

Final result: dp[13] = True

'''
