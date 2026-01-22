class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start
        intervals.sort()
        # Sort queries with original indices. index to use to populate res
        sorted_queries = sorted((q,i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        heap = [] # (interval_length, interval_end)
        i=0 # pointer for intervals

        for q,idx in sorted_queries:
            # Add intervals whose start <= q
            while i < len(intervals) and intervals[i][0]<=q:
                l,r = intervals[i]
                heapq.heappush(heap,(r-l+1,r))
                i+=1
            # Remove intervals that end < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            # Top of heap is the smallest valid interval
            if heap:
                res[idx] = heap[0][0]
        return res
