class solution:
  def minMeetingRooms(intervals):
      if not intervals:
          return 0
  
      intervals.sort(key=lambda x: x[0])  # sort by start time
      heap = []  # min-heap of end times
  
      for start, end in intervals:
          if heap and heap[0] <= start:
              heapq.heappop(heap)
          heapq.heappush(heap, end)
  
      return len(heap)
