class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [set() for _ in range(n)]

        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        # 1) Remove all leaf nodes that have no coin
        q = deque(i for i in range(n) if len(g[i]) == 1 and coins[i] == 0) #len(g[i]) is to find the leaf node

        while q:
            i = q.popleft()
            for j in list(g[i]):
                g[j].remove(i)
                if len(g[j]) == 1 and coins[j] == 0:
                    q.append(j)
            g[i].clear()

        # 2) Remove two layers of leaves
        for _ in range(2):
            leaves = [i for i in range(n) if len(g[i]) == 1]
            for i in leaves:
                for j in list(g[i]): #list so that you can iterate over its neighbors
                    g[j].remove(i)
                g[i].clear()

        # Count remaining edges
        remaining_edges = sum(len(adj) for adj in g) // 2 #since the edges are added both the ways. 'undirected graph'
        return remaining_edges * 2
    
'''
The problem says you can start at any vertex, and each move is either: collect all coins within distance at most 2 from your current vertex, or move to an adjacent vertex. The goal is to collect all coins and return to the starting vertex with the minimum number of edge traversals.

The greedy solution is to prune the tree in two stages: first remove every leaf with no coin until none remain, then remove two rounds of leaves from the remaining tree. After that, every edge left must be traversed twice, so the answer is 2 * remaining_edges. This is the topological-trimming approach described in the official-style explanation.

Why this works

The first pruning step removes dead ends that can never help collect a coin. After that, every remaining leaf has a coin. Then, because coins can be collected from distance 2, the outer two layers of the tree do not need to be traversed at all, leaving only the “core” edges that must be walked both ways.

Complexity

The trimming process is linear in the number of nodes and edges, so the solution runs in O(n) time and O(n) space.

'''
