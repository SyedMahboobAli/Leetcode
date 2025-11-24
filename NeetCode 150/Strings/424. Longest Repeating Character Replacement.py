class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        maxf = 0 #count most freq char in curr window
        res = 0

        n=len(s)
        l=0

        for r in range(n): #expand window by moving r pointer
            count[s[r]] = count.get(s[r],0) + 1
            #maxf will already have till the prev char, since we updated s[r] count, only check with that
            maxf = max(maxf,count[s[r]])
            # (window size - count of most frequent char > k)
            while((r-l+1) - maxf) > k :
                #shrink window from left
                count[s[l]] -= 1
                l+=1
            #Update the result with the maximum valid window size
            res = max(res,r-l+1)
        return res

