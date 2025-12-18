# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Recursive DFS
        if not p and not q:  #both nodes are None, structure matches,subtree is identical.
            return True
        if not p or not q: #the structure is different.
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
