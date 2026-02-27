'''
At every step:
If n is even → divide by 2
If n is odd:
If last two bits are 11 → add 1 and increase res
Otherwise last two bits are 01 → subtract 1 and increase res
That’s it.
'''
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif (n & 3) == 3:
                n += 1
                res += 1
            else:
                n -= 1
                res += 1
        return res
