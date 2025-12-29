"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: #imp as this will cause error n.val not found
            return None
            
        # Map original node -> cloned node
        cloned = {}

        def dfs(n):
            if n in cloned:
                return cloned[n]
            
            copy = Node(n.val)
            cloned[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)
        
