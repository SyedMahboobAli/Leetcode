class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        most_water=0
        while(l<r):
            area = min(height[l],height[r])* (r-l)
            most_water=max(most_water,area)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return most_water
