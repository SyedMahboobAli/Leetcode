class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        need = Counter(t)
        window = {}

        res = [-1,-1]
        resLen = float('inf')

        have = 0
        needCount = len(need)
        l=0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            #increase have if s[r] is in need
            if s[r] in need and window[s[r]] == need[s[r]]:
                have+=1

            #all requirements met, decrease window
            while have == needCount:
                #first save the values if less then prev
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                    
                #window shrinking
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have-=1
                l+=1

        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""
