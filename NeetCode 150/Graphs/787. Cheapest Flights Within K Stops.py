class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adjacency list: u -> [(v, cost), ...]
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        # best[node][stops_remaining] = min cost
        best = dict()
        # min-heap: (cost, node, stops_remaining)
        heap = [(0,src,k+1)]

        while heap:
            cost, node, stops = heapq.heappop(heap)
            # if reached destination, return cost
            if node == dst:
                return cost
             # if no stops left, can't go further
            if stops>0:
                for nei,price in graph[node]:
                    new_cost = cost + price
                    # If we haven't visited (nei, stops-1) or we found a cheaper cost
                    if (nei,stops - 1) not in best or best[(nei,stops - 1)] > new_cost:
                        best[(nei,stops - 1)] = new_cost
                        heapq.heappush(heap,(new_cost,nei,stops - 1))
        return -1
