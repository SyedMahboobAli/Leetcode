class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(' , '}' : '{' , ']' : '['}
        for ch in s:
            if ch in mapping:
                top_element = stack.pop() if stack else '#' #ensure this condition
                if mapping[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return not stack #if stack is empty we want true
