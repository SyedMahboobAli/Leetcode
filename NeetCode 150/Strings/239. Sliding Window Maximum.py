class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() #stores index
        res = []
        for i in range(len(nums)):
            # Remove elements out of this window
            #since we are moving one step at a time, only one element removal is fine and while loop not needed
            if dq and dq[0] == i-k:# i - k will give window. k is len and i is index for 0 to n-1. so i-k will give left element outside window
                dq.popleft()
            
            # Remove smaller elements (useless)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            # Start adding results once we reach size k
            if(i>=k-1):
                res.append(nums[dq[0]]) # we add 0th index dq number as this will always be a montonically decreasing queue
        return res
'''
check needcode video for understanding
ex:
Window	Elements	Max
Window 1	[8, 7]	8
Window 2	[7, 6]	7
Window 3	[6, 9]	9
'''
