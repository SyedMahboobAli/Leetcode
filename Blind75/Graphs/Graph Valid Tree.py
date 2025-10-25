class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # For a graph to be a tree:
        # 1. It must be fully connected (all nodes reachable)
        # 2. It must have no cycles
        # 3. It must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list representation of the graph, and we are using [[]] because the vertices are from 0 to n-1 and not different numbers/letters. then we would use dictionary
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
'''
Notes:
BFS answer:

from collections import deque

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = [False]*n
        # BFS from node 0
        q = deque([0])
        seen[0] = True
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                if not seen[nei]:
                    seen[nei] = True
                    q.append(nei)

        return count == n  # all nodes reachable

We are not using parent here

In this specific BFS implementation, it doesn’t explicitly check for cycles, because the len(edges) != n-1 check already guarantees:

If there are more than n-1 edges → there must be a cycle.

If there are fewer than n-1 edges → graph is disconnected.

So with n-1 edges, the only remaining condition to check is connectivity, which the BFS does via count == n.

✅ If the graph is connected and has exactly n-1 edges, it must be a tree.
No explicit cycle check needed!

✅ BFS doesn’t need a parent argument because it never revisits nodes (due to seen[]), and the len(edges) == n-1 condition already rules out cycles.
'''
