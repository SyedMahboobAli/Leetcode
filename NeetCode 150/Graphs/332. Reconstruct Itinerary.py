class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Graph where:
        # key   = source airport
        # value = min-heap of destination airports
        # Min-heap ensures lexicographically smallest destination is chosen first
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src],dst)
        # This will store the itinerary in reverse order
        route = []

        def dfs(airport):
            while graph[airport]:
                """
            Hierholzer's DFS:
            - Keep visiting next smallest destination
            - Remove (use) each ticket exactly once
            - Add airport to route ONLY after all outgoing edges are used
            """
                # Choose the lexicographically smallest destination
                new_airport = heapq.heappop(graph[airport])
                dfs(new_airport)
            # Postorder insertion:
            # When no outgoing edges remain, add airport to route
            route.append(airport)
        
        dfs("JFK")
        return route[::-1]  # Reverse because we added airports after exhausting all flights
