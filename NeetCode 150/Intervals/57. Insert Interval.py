class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        start , end = newInterval
        res = []

        while i<n and intervals[i][1] < start:
            res.append(intervals[i])
            i+=1
        
        while i<n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i+=1
        res.append([start,end])

        while i<n:
            res.append(intervals[i])
            i+=1

        return res
        
