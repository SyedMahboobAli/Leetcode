class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])
        # Initialize the result list with the first interval
        result=[intervals[0]]

        for start, end in intervals[1:]:
            #End value of latest added value in the result
            lastEnd = result[-1][1]

            # If the current interval overlaps with the last interval in result, Merge by updating the end of the last interval
            if(start <= lastEnd):
                result[-1][1]=max(lastEnd,end)
            else:
                result.append([start,end]) # No overlap, so just append the current interval
        
        return result
