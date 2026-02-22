class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res= [intervals[0]]
        
        for start,end in intervals:
            last_end= res[-1][1]
            if start <= last_end:
                res[-1][1] = max(last_end,end)
            else:
                res.append([start,end])
        return res
