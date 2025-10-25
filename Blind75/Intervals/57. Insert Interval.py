class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i=0
        n=len(intervals)
        res=[]
        start,end=newInterval[0], newInterval[1]

        # Add all intervals that come before the new interval, we don't want overlap here strictly <
        while i<n and intervals[i][1] < start:
            res.append(intervals[i])
            i+=1
        #Merge all overlapping intervals, so we use <= because we need to include all that is within
        while i<n and intervals[i][0] <= end:
            start = min(start,intervals[i][0])
            end = max(end,intervals[i][1])
            i+=1
        res.append([start,end])# Add the merged interval
        #Add all intervals that come after the merged one
        while i<n:
            res.append(intervals[i])
            i+=1
        
        return res
