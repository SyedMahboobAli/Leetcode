#Sol: Use two stacks. One main and the other min_stack
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min stack empty OR new val <= current min, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        # If popped is current minimum, remove from min stack
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
