class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Step 1: Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Check for overlap
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        
        return True
