class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #RPN (Reverse Polish Notation) means operators come after operands:
        stack = []
        
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b=stack.pop()
                a=stack.pop()

                if t == '+':
                    stack.append(a+b)
                elif t == '-':
                    stack.append(a-b)
                elif t == '*':
                    stack.append(a*b)
                else:#division
                    # The problem specifies truncation toward zero
                    stack.append(int(a/b))
        return stack[-1]
'''
Expression	    Python a//b	    Required	int(a/b)
-7 / 3	        -3	            -2	        -2
'''
        
