class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[1])

        last_end = float('-inf')
        removal_count = 0

        for start,end in intervals:
            if start < last_end:
                removal_count += 1
            else:
                last_end = end
        
        return removal_count
