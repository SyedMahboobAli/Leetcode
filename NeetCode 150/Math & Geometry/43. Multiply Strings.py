class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 =="0":
            return "0"
        
        m,n = len(num1),len(num2)
        res = [0] * (m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")
                mul = digit1*digit2

                p2 = i+j+1 #curr digit pos
                p1 = i+j #carry

                total = mul + res[p2]

                res[p2] = total %10 #cur digit
                res[p1] += total //10 #carry, add to previous. it will already have a value
        #convert arr to string
        result = []
        for digit in res:
            if not result and digit == 0:
                continue
            result.append(str(digit))
        
        return "".join(result)

