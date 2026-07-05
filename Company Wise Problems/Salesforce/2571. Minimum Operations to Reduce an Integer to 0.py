'''
At every step:
If n is even → divide by 2
If n is odd: then last 2 digits of odd can be 11 or 01
If last two bits are 11 → add 1 and increase res
Otherwise last two bits are 01 → subtract 1 and increase res
That’s it.
'''
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1 #this is divide by 2. Since we can do this any number of times (power of 2 times) we are not incrementing res and also when we add or subtract from 'n' only then the operation is counted. now in the next scenarios for odd, we are only incrementing 1 or decrementing 1. imagine that here we are subtracting 2 power x and then also subtracting 2 power 0. cumulative that operation is 1. 
            elif (n & 3) == 3:
                n += 1
                res += 1
            else:
                n -= 1
                res += 1
        return res
