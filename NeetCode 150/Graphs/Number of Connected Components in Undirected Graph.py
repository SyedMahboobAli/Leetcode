class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Edge case: no nodes → no components
        if n == 0:
            return 0
        
        # Build adjacency list for undirected graph
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # Visited array to track nodes already explored
        visit = [False] * n

        # Depth-First Search (DFS) to explore all nodes in one component
        def dfs(node):
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
        
        comp = 0  # counts number of connected components
        
        # Loop over all nodes
        for i in range(n):
            # If a node is not visited, start DFS — new component found
            if not visit[i]:
                comp += 1
                dfs(i)

        return comp   


