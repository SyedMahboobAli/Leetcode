class MedianFinder:

    def __init__(self):
        self.low = [] # max-heap (store -value)
        self.high = [] # min-heap
        

    def addNum(self, num: int) -> None:
        # push to low
        heapq.heappush(self.low, -num)

        # move the largest from low to high so that all low <= all high
        val = -heapq.heappop(self.low)
        heapq.heappush(self.high, val)

        # keep sizes balanced so low can have one extra element at most
        if len(self.high) > len(self.low):
            moved = heapq.heappop(self.high)
            heapq.heappush(self.low,-moved)
        
    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        else:
            return (-self.low[0] + self.high[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
