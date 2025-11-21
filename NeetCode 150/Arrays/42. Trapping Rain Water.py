class Solution:
    def trap(self, height: List[int]) -> int:
        #approach 2: 2 pointer
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        leftmax = height[l]
        rightmax = height[r]
        water = 0 

        while (l<r):
            #Whichever side has the smaller boundary will decide how much water can be trapped and we add water one index at a time
            if leftmax < rightmax:
                #we are doing l+ here and r- first as we are not including the edges => 0 and n-1 index. At the edges (first and last index), there is no boundary on one side, so they can never trap water. even if we use the formula we get 0. so no use. hence skipping.
                l += 1
                leftmax = max(leftmax,height[l]) # this will have highest until now and also will handle next line where leftmax - height[l] will not go -ve if height[l] is more and leftmax is left. so we are not adding -ve to water
                water += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax,height[r])
                water += rightmax - height[r]              
        return water


        #approach 1: brute force
        if not height:
            return 0
        water = 0
        n = len(height)

        for i in range(n):
            leftmax = rightmax = height[i]
            #check max on left side of the curr pos
            for j in range(i):
                leftmax = max(leftmax,height[j])
            #check max on right side of curr pos
            for j in range(i+1,n):
                rightmax = max(rightmax,height[j])
            #select min of both the max and remove from curr height
            #Whichever side has the smaller boundary will decide how much water can be trapped:
            water +=min(leftmax,rightmax) - height[i]
        
        return water
