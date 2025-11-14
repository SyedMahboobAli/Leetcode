Soltion 2: Heap. Most Optimum
class MedianFinder:

    def __init__(self):
        # low is a max-heap implemented by pushing negatives
        self.low = []  # max-heap (store -value)
        self.high = [] # min-heap

    def addNum(self, num: int) -> None:
        """
        Add number into data structure.
        Strategy:
        - Push into low (max-heap) first (as -num).
        - Pop the largest from low and push it into high to ensure every element
          in low <= every element in high.
        - If high has more elements than low, move smallest from high back to low.
        This keeps sizes balanced and ordering invariant.
        """
        # push to low (max-heap via negative)
        heapq.heappush(self.low,-num)

        # move the largest from low to high so that all low <= all high
        val = -heapq.heappop(self.low)
        heapq.heappush(self.high,val)

        # keep sizes balanced so low can have one extra element at most
        if (len(self.high) > len(self.low)):
            moved = heapq.heappop(self.high)
            heapq.heappush(self.low, -moved)

    def findMedian(self) -> float:
        """
        Return median:
        - If total count is odd, low has one extra element → median = top(low)
        - If even, median = (top(low) + top(high)) / 2
        """
        if(len(self.low) > len(self.high)):
            return float(-self.low[0])
        else:
            return (-self.low[0] + self.high[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

Solution 1: Sorting
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n =len(self.data)
        return (self.data[n//2] if (n & 1) else (self.data[n//2] + self.data[n//2 -1]) /2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
