# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque()
        q.append(root)
        #instead of above 2 lines, have only one line as q=deque([root]). this is only one root node added and not list.
        while q:
            level = [] # Holds nodes of the current level
            for _ in range(len(q)): # Process all nodes in this level
                node = q.popleft()
                level.append(node.val)
                 # Add child nodes for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level) # Add current level to result
        return res

        
