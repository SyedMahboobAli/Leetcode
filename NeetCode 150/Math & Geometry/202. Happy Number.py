class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            total = 0
            while x>0:
                d = x%10
                total += d*d
                x //= 10
            return total
        
        slow = next_num(n)
        fast = next_num(next_num(n))

        while fast!=1 and slow!=fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        
        return fast == 1
