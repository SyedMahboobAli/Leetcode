
#Topological Sort Kahn's algo BFS
from collections import deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize adjacency and indegree maps
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Invalid prefix case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the first differing character
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # Step 3: Topological sort using Kahn’s Algorithm (BFS)
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # Step 4: Check for cycles
        if len(res) != len(indegree):
            return ""

        return "".join(res)
