class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        
        #solution 2, 
        #best and understable, ex 1001, 1001>>1 = 100 we already stored this value in dp[4] so the last bit that came out, we check if it is one or 0 and add it in current dp
        for i in range(1,n+1):
            dp[i]=dp[i>>1] + (i&1)
        return dp

        #solution 1
        #little complicated but different. 
        # logic: for 1001, we divide as 1 | 001, so we add 1 always to dp[001] i.e dp[1]
        # so offset is always multiple of two, dp[i-offset], will give us dp[001] 
        offset=1
        for i in range(1,n+1):
            if(offset*2==i):
                offset=i
            dp[i]=1+dp[i-offset]
        return dp
