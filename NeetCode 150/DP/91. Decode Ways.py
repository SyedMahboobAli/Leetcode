class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] *(n+1)
        if n == 0:
            return 0
        dp[0] = 1 #base case for dp
        dp[1] = 0 if int(s[0]) ==0 else 1

        for i in range(2,n+1):
            one_digit = int(s[i-1:i]) #i of dp is i-1 in s
            two_digit = int(s[i-2:i])

            if (1<=one_digit<=9):
                dp[i] += dp[i-1]
            if (10<=two_digit<=26):
                dp[i] += dp[i-2]
        return dp[n]
