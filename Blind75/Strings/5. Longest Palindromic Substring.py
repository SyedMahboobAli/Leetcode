 ''' 
        2 pointer solution
        We consider each index as a potential center and expand left & right:

Odd-length palindromes → center at one character (e.g., "aba")

Even-length palindromes → center between two characters (e.g., "abba")

We check both for each index.
        '''
        res="" # To store the longest palindrome
        resLen=0 # Length of the longest palindrome
        n=len(s)

        for i in range(n):
            # Check for odd-length palindrome
            l,r = i , i
            while l>=0 and r<n and s[l]==s[r]:
                if(r-l+1 > resLen):
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1

            # Check for even-length palindrome
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                if(r-l+1 > resLen):
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res

#DP solution is also O(n2) : just for info. go for 2 pointer only since memory optimized
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        for i in range(n - 1, -1, -1):  # Start from end (bottom-up)
            for j in range(i, n):
                # Palindrome if chars match and either:
                # 1) length < 3 (1 or 2 chars) or
                # 2) inner substring is palindrome
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                # Update result if this is longest palindrome found
                if dp[i][j] and (len(res) < j - i + 1):
                    res = s[i:j + 1]
        return res
