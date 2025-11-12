# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #approach 2 : iteration. Iteration is better wrt to time

        while root:
            if (p.val<root.val and q.val<root.val):
                root=root.left
            elif (p.val > root.val and q.val > root.val):
                root=root.right
            else:
                return root
        #Approach 1: recursion
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        return root
