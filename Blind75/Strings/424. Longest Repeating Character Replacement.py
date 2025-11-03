class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to count frequency of characters in the current window
        count={}
        # maxf will store the count of the most frequent character in the current window
        maxf=0

        n=len(s)
        l=0
        res=0
        
        # Expand the window by moving the right pointer
        for r in range(n):
            # Increase the frequency count of the current character, .get(s,0) set default to 0 if not present
            count[s[r]] = count.get(s[r],0) + 1
            # Update the maximum frequency in the current window, maxf will already have till the prev char, since we updated s[r] count, only check with that
            maxf = max(maxf,count[s[r]])

            # Check if the number of replacements needed exceeds k
            # (window size - count of most frequent char > k)
            while (r-l+1)-maxf > k : 
                # If invalid, shrink the window from the left
                count[s[l]]-=1
                l+=1
            # Update the result with the maximum valid window size
            res = max(res,r-l+1)

        return res
