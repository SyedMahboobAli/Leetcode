class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {')' : '(' , '}' : '{' , ']' : '['} # Map closing to opening brackets

        for char in s:
            if char in mapping:
                # Pop from stack if not empty, else assign dummy value '#'
                top_element = stack.pop() if stack else '#'
                # Check if popped element matches expected opening bracket
                if (mapping[char] != top_element):
                    return False
            else:
                 # It's an opening bracket, push onto stack
                stack.append(char)      
        # If stack is empty → all brackets matched properly
        return not stack
            
