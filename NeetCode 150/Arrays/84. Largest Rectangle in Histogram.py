class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Sol 1:Monotonic increasing stack easy to understand solution same complexity 
        stack = []
        max_area = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i # by default, the rectangle can start at i

            # While the stack has bars and the previous bar height is greater than current height
            # pop it because its rectangle must end before this index
            while stack and stack[-1][1] > h:
                j , height = stack.pop() # j = start index of that bar; height = its height

                width = i - j # width extends from j up to i
                max_area = max(max_area,height*width)

                # Important: the popped bar's start index becomes the new start
                # for current height h (since h can extend leftward to j)
                start = j

            # Push the current bar with the farthest possible left boundary (start)
            stack.append((start, h)) 

        # Now empty the stack for bars that extend till the end of the array, because you will have tuples still present
        while stack:
            i , height = stack.pop()
            max_area = max(max_area , height* (n-i)) # width = n - i as current index is n and from there we are computing till the farthest left boundary
        
        return max_area
