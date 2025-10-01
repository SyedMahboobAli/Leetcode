class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for _ in range(32):
            last_bit=n&1
            result<<=1
            result|=last_bit
            n>>=1
        return result
