# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Approach 1: Recursive DFS
        if not root:
            return None

        # Swap left and right children
        root.left,root.right = root.right,root.left

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        #Approach 2: BFS
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            # Swap children
            node.left,node.right = node.right,node.left
            # Add children to queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root
