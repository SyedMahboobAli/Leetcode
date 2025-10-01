

class Solution:
    def hammingWeight(self, n: int) -> int:
        #sol 3
        #return bin(n).count('1')

        #sol 2
        count=0
        while(n):
            n=n&(n-1) # n&=n-1
            count+=1
        return count

        #solution 1
        count=0
        while(n):
            count+=n&1 #or count+=n%2
            n>>=1
        return count
