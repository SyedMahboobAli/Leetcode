class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Solution : BFS + MinHeap
        n = len(points)
        #build adj list
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)

                adj[i].append((dist,j))
                adj[j].append((dist,i))
        #Prim's Algo
        res = 0
        visit = set()
        min_heap = [(0,0)] #cost,point
        while len(visit) < n: #ensure the condition is diff and we are not checking min_heap instead
            cost,i = heapq.heappop(min_heap)
            if i in visit:
                continue
            res += cost #we are adding the cost to the result only here
            visit.add(i)
            for neiCost,nei in adj[i]:
                #If already in visit. added to res already, so don't add
                if nei not in visit:
                    heapq.heappush(min_heap,(neiCost,nei)) 
                    #we are only adding curr dist and not sum with previous.
                    
        return res
