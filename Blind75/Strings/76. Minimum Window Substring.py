class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # Count how many of each character we need from t
        need = Counter(t) #from collections import Counter
        # Current window character counts
        window = {}

        l=0
        resLen = float("inf") # length of smallest valid window
        # Result variables to store the best (smallest) window found
        res=[-1,-1]# store indices [left, right]

        # 'have' = how many unique chars currently satisfy the requirement
        # 'needCount' = how many unique chars total are needed
        have=0
        needCount=len(need) # we are not using len(t) coz they might have dup


        for r in range(len(s)):
            c=s[r]
            window[c] = window.get(c,0) + 1
            # If this char’s count matches what we need → one requirement fulfilled
            if c in need and window[c] == need[c]:
                have+=1
            
            # Try to shrink window from the left if all requirements are met
            while have == needCount:
                # Update result if this window is smaller than previously found
                if(r-l+1 < resLen):
                    res = [l,r]
                    resLen = r-l+1

                # Remove leftmost character from the window
                window[s[l]] -= 1
                # If removing it breaks the requirement, decrease 'have'
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have -= 1
                # Move left pointer to shrink window
                l+=1

        l,r=res
        return s[l:r+1] if resLen != float("inf") else ""
