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
        #base case
        if not node:
            return None

        # Map original node -> cloned node. Key is original node and value is copy node
        cloned = {}

        def dfs(n):
            #if already visited return the copy
            if n in cloned:
                return cloned[n]
            
            # Clone the node
            copy=Node(n.val)
            cloned[n]=copy

            # Clone all neighbors recursively
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        
        return dfs(node)

        
