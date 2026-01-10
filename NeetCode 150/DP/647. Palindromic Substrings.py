class Solution:
    def countSubstrings(self, s: str) -> int:
        #2 pointer is the best sol
        n =len(s)
        res = 0 
        def explore(l,r):
            count = 0
            while(l>=0 and r<n and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            return count
        
        for i in range(n):
            res += explore(i,i)#odd len
            res += explore(i,i+1)#even len
        return res
