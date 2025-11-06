# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float("-inf") #Using self.res makes it an instance variable, accessible in both functions:
        # Or use in dfs,
        #nonlocal res   # Tell Python to use outer variable

        def dfs(node):
            if not node:
                return 0
            # Max path sum from left and right subtrees (ignore negatives)
            left_gain = max(0,dfs(node.left))
            right_gain = max(0,dfs(node.right))

            # Price of the new path that passes through this node
            price_newpath = node.val + left_gain + right_gain
             # Update global maximum
            self.res = max(self.res,price_newpath)

            # Return the max gain from this node upwards (single branch)
            return node.val + max(left_gain,right_gain)
        
        dfs(root)
        return self.res

