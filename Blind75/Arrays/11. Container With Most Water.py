#11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        res,l,r=0,0,n-1
        while(l<r):
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return res
