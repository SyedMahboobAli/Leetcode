class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Solution is BFS + Min Heap
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        
        min_heap = [(0,k)] #We are not using queue in BFS, we are using min_heap
        time = 0
        visit = set()
        while min_heap:
            w1,n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = max(time,w1)
            #in Heap we have w,n and in adj list we have n,w
            for n2,w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap,(w1+w2,n2))
                    
        return time if len(visit) == n else -1


