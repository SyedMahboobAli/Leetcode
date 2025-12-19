# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #solution is inorder traversal. You can also add a arr for res and return res[k-1] in the end
        res = root.val
        count = k

        def dfs(node):
            nonlocal res,count
            if not node:
                return 
            
            dfs(node.left)
            count -= 1
            if count == 0:
                res = node.val
                return 
            dfs(node.right)

        dfs(root) 
        return res
