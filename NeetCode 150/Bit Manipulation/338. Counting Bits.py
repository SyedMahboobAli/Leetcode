class Solution:
    def countBits(self, n: int) -> List[int]:
        #sol2
        dp = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if(offset*2==i):
                offset = i
            #for i = 1 it would add 1 below
            dp[i] = 1 + dp[i-offset] #1001=> 1 001 => so 1 +  dp[i-offset]
        return dp
        #sol1
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i>>1] + (i&1)
        return dp
