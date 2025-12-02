class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        A monotonic decreasing stack is a stack where the values stored (or the values pointed to) are always in strictly decreasing order from bottom to top.
        In other words: Each new element you push must be ≤ the element at the top of the stack. If it's larger, you pop until the condition is restored.
        '''
        n = len(temperatures)
        res = [0] * n
        stack = [] # stores indices

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
'''
ex:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Step	i	T[i]	Stack(values before)	Action	                            Stack after	res
1	    0	30	    []	                    Push 30	                            [30]        [0,0,0]
2	    1	60	    [30]	                60 > 30 → pop 0 → res[0]=1	Push 60	[60]        [1,0,0]
3	    2	90	    [60]	                90 > 60 → pop 1 → res[1]=1	Push 90	[90]        [1,1,0]

'''
