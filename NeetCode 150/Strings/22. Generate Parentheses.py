class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #this is to generate all combination. So Backtracking is the best sol
        #1. Only add open parathesis if open < n
        #2. Only add a close paranthesis if close < open
        #3. Valid if open == close == n (base case)
        stack = []
        res = []

        def backtrack(open,close):
            if open == close == n:
                res.append("".join(stack))

            if open < n:
                stack.append('(')
                backtrack(open+1,close)
                stack.pop()
            
            if close < open:
                stack.append(')')
                backtrack(open,close+1)
                stack.pop()

        backtrack(0,0)
        return res     
