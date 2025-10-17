class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if(n==0):
            return 0 
            #empty string 0 ways
        dp=[0]*(n+1)
        dp[0]=1 #we are already returning 0 for len 0, this 1 is to the base case for dp to start the calculation
        dp[1]=0 if int(s[0])==0 else 1
        for i in range(2,n+1):
            one_digit=int(s[i-1:i]) # in dp[1] we are storing s[0], so i in dp is i-1 in s
            two_digits=int(s[i-2:i])

            if(1<=one_digit<=9):
                dp[i]+=dp[i-1]
            if(10<=two_digits<=26):
                dp[i]+=dp[i-2]
            
            '''
            example: s=1111
Single-digit case (dp[i-1]):

'111' + '1'

We take all valid decodings of s[:i-1]

Then we append one single letter formed by s[i-1]

e.g. decoding "111" → "AAA", "AK", "KA", then append "1"→A"

=> "AAAA","AKA","KAA". Then count is still 3, so we take total 3 into consideration so dp[i]+=dp[i-1]

Two-digit case (dp[i-2]):

"11" +"11"

We take all valid decodings of s[:i-2]

Then we append one single letter formed by s[i-2:i] (the last two digits)

e.g. decoding "11" → "AA", "K", then append "11"→K"

=> "AAK","KK". The count is is still 2 which is of dp[2], we are just adding another letter to it. so we add dp[i]+=dp[i-2]

both these sets are disjoint. so need to add both

            '''
        return dp[n]
