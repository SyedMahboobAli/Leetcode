# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Solution 2 : Serialize trees + substring search
        root_ser = self.serialize(root)
        sub_root_ser = self.serialize(subRoot)
        return sub_root_ser in root_ser # substring check , # could use KMP for guaranteed O(|s_ser|+|t_ser|)

    def serialize(self,s):
        if not s:
            return ",#"
        return "," + str(s.val) + self.serialize(s.left) + self.serialize(s.right) # similar to pre order traversal
        #check last lines for other simplified approach
        #Solution 1 : Recursion DFS
        if not root:
            return False #we are checking t in s. To check t == subtree of s we use diff func. Here it is different
        if self.isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def isSameTree(self,s,t):
        if not s and not t:
            return True
        if not s or not t or s.val !=t.val:
            return False
        if(self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)):
            return True
        
        '''
    Other simplified but same serialize function
    res = []
    def dfs(node):
        if node is None:
            res.append(",#")  # null marker
            return
        res.append("," + str(node.val))  # prefix comma to avoid digit run-together
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return "".join(res)
    '''

        
