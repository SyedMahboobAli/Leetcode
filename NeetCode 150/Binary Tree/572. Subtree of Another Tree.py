# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) #ensure it is subtree and not sametree
            #isSameTree(a, b) only checks exact structural equality at that node.
            #isSubtree(a, b) checks whether b exists anywhere inside a.
    
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
    #Other approach is serializable which is converting to strings and checking if one string in another.Check Blind75 notes
     '''
    def serialize(self,s):
        if not s:
            return ",#"
        return "," + str(s.val) + self.serialize(s.left) + self.serialize(s.right) # similar to pre order traversal
    
    in subtree func:
        root_ser = self.serialize(root)
        sub_root_ser = self.serialize(subRoot)
        return sub_root_ser in root_ser # substring check , # could use KMP for guaranteed O(|s_ser|+|t_ser|)
    '''
