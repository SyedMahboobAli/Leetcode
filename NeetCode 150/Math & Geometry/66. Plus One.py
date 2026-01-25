class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        plus_one = int(num) + 1
        res = []
        for s in str(plus_one):
            res.append(int(s))
        return res
