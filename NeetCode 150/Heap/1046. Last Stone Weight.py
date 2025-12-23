class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            y = heapq.heappop(heap) #x <= y
            x = heapq.heappop(heap)

            res = y - x
            if res:
                heapq.heappush(heap,res)
        
        return -heap[0] if heap else 0
        # there is a possibility of all stone destroyed
        # stones = [5,5]

        
