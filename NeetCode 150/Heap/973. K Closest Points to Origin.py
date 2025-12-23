class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = (x**2) + (y**2) #Since square root doesn’t change ordering, we use this
            heapq.heappush(heap,(-distance,[x,y]))
            #we need a max heap as we need to pop farthest not closest
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for dis,point in heap] # we are only using point and not dis, but we are traversing through dis,point because both are present in heap
