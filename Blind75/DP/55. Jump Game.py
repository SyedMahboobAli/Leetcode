class Solution:
    def canJump(self, nums: List[int]) -> bool:
                #Greedy Solution is the best solution

        n=len(nums)
        # max_reach is the farthest index we can reach so far
        max_reach=0

        for i,jump in enumerate(nums):
            # if current index is beyond what we can reach, fail
            if(i>max_reach):
                return False
            # extend max_reach using jump at i
            max_reach=max(max_reach,i+jump)
             # early success
            if(max_reach>=n-1):
                return True
            
        return max_reach>=n-1


        #other greedy approach:
        n=len(nums)
        goal=n-1
        for i in range(n-1,-1,-1):
            if((i+nums[i])>=goal):
                #keep moving the goal left because the current index is reached
                goal=i
        
        return True if (goal==0) else False
        #DP solution, slower. This will give TLE error. Greedy is the best
        '''we do a bottoms up approach/traverse from last element because dp[i] true only if from that index we can reach last index'''
        n=len(nums)
        dp=[False]*n
        dp[n-1]=True
        '''
        for i in range(n-2,-1,-1):
            if(nums[i]+i>=n-1):
                dp[i]=True
            else:
                if(dp[i+nums[i]]):
                    dp[i]=True

        the issue above is with the else
        if(dp[i+nums[i]]):
            dp[i]=True

        this will check only one element but we can reach all the next nums[i] elements, and if any of that is true, it means this is true
        '''
        for i in range(n-2,-1,-1):
            furthest_element = min(i+nums[i],n-1) # if furthest goes more that n-1, then index array out of bound
            for j in range(i+1,furthest_element+1):
                if dp[j]:
                    dp[i]=True
                    break
            
        return dp[0]


        
