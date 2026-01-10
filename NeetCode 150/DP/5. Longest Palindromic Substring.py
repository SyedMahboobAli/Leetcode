class Solution:
    def longestPalindrome(self, s: str) -> str:
        #2 pointer is a better soluion
        res = ""
        resLen = 0
        n = len(s)

        for i in range(n):
            l,r = i,i #odd len palindrome check
            while l>=0 and r<n and s[l] == s[r]:
                if(r-l+1 > resLen):
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            
            l,r = i,i+1 #even len palindrome check
            while l>=0 and r<n and s[l] == s[r]:
                if(r-l+1 > resLen):
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            
        return res
