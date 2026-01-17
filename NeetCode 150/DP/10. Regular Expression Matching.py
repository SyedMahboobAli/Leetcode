class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]

        #Base cases
        dp[0][0] = True
        for j in range(2,n+1): #* handling. patterns like a*,a*b*,...
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2] #for zero ocurrance
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    #Zero occurrance
                    dp[i][j] = dp[i][j-2]

                    #one or more occurrence
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]
        

        

