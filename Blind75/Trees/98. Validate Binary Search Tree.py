# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,low,high):
            # Base case: empty tree is valid
            if not node:
                return True
            # If node violates the BST property
            if not(low < node.val < high):
                return False
            
            # Left subtree: valid range becomes (low, node.val)
            # Right subtree: valid range becomes (node.val, high)
            return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
        
        # Start with the full possible range
        return dfs(root,float('-inf'),float('inf'))
