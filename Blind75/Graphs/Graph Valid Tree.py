class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # For a graph to be a tree:
        # 1. It must be fully connected (all nodes reachable)
        # 2. It must have no cycles
        # 3. It must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list representation of the graph
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()  # to keep track of visited nodes during DFS

        def dfs(node, parent):
            """
            Returns False if a cycle is detected, otherwise True.
            'parent' is used to avoid falsely detecting a cycle
            through the immediate parent in an undirected graph.
            """
            if node in visit:
                return False  # visiting an already visited node → cycle detected

            visit.add(node)

            # Explore all adjacent (neighboring) nodes
            for nei in adj[node]:
                if nei == parent:
                    continue  # skip the parent to prevent false cycle detection
                if not dfs(nei, node):
                    return False  # cycle detected deeper in recursion

            return True  # no cycle found from this node

        # Start DFS from node 0 (graph is assumed to have nodes 0..n-1)
        # If a cycle is found, return False immediately
        if not dfs(0, -1):
            return False

        # After DFS, check if all nodes were visited (ensures connectivity)
        return len(visit) == n
