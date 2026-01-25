class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:#handle -ve
            x = 1/x
            n = -n
        result = 1
        while n>0:
            #handle odd, only this would store in result 
            if n % 2 == 1:
                result *= x
            
            x *= x
            n //= 2
        return result
