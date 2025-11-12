# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #approach 2 memory optimized. 
        res = root.val
        count = k

        def dfs(node):
            nonlocal res,count
            if not node:
                return 
            
            dfs(node.left)
            count-=1
            if count==0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res

        #approach 1 inorder traversal, sorted array returned
        res = [] # array , so no self or nonlocal needed

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res[k-1] # 1-indexed

'''
# in recursion solution, we can also do this to stop storing more values in the array
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
'''
