class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def isPalindrome(l,r):
            while (l<r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(start):
             # If we've used the entire string, record the partition
            if start == len(s):
                res.append(subset[:]) # make a copy
                return
             # Try all possible end positions
            for end in range(start,len(s)):
                if isPalindrome(start,end):
                    subset.append(s[start:end+1])
                    backtrack(end+1)
                    subset.pop()

        backtrack(0)
        return res
