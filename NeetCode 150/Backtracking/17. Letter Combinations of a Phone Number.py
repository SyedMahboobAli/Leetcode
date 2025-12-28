class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        subset = []
        # we can also use "2" as string for key
        phone = {2:"abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        #you can't initialize subset above since we are using pointers and strings. So it must be sent using function
        def backtrack(idx):
            # If we've used all digits, path is a complete combination
            if idx == len(digits):
                res.append("".join(subset)) #since this is a string don't need a copy
                return
            # Get letters for the current digit
            letters = phone[int(digits[idx])]

             # Try each letter
            for ch in letters:
                subset.append(ch)
                backtrack(idx + 1)
                subset.pop()

        backtrack(0)
        return res
