class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 -1
        rev = 0 
        sign = -1 if x<0  else 1
        x = abs(x)
        while x:
            digit = x %10
            x //= 10
            rev = rev*10 +digit
        
        rev *= sign

        if rev<INT_MIN or rev>INT_MAX:
            return 0
        return rev
