class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else: #'*
                low -= 1
                high += 1
            if high<0: #invalid, more )
                return False
            low = max(low,0)
        
        return low == 0 #at end low should be 0

