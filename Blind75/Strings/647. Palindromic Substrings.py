class Solution:
    def countSubstrings(self, s: str) -> int:
        #2 pointer best solution
        n=len(s)
        res=0

        def explore(l,r):
            count=0
            while l>=0 and r<n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            return count

        #explore from every char at i
        for i in range(n):
            res+=explore(i,i)# Odd length
            res+=explore(i,i+1)# Even length
        return res

        #DP solution. O(n2) not memory optimized
        n=len(s)
        dp=[[False]* n for _ in range(n)]
        count=0

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j]=True
                    count+=1
        return count
            
        
