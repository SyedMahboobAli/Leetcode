# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Approach 1: Recursive DFS : Best
        if not root:
            return 0
        return 1 + (max(self.maxDepth(root.left),self.maxDepth(root.right)))

        #Approach 2: Iterative Stack DFS
        if not root:
            return 0

        stack = [(root, 1)]  # (node, current depth)
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth

        #Approach 3: BFS
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Increment depth after each level
            depth += 1
        
        return depth
