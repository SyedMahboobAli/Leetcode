class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # Sort intervals by their end times
        intervals.sort(key=lambda x:x[1])

        last_end = float('-inf')
        removal_count=0

        for start,end in intervals:
            # Overlap, need to remove this interval
            if start < last_end:
                removal_count+=1
            else:
                # No overlap, update end
                last_end=end
        
        return removal_count
        
