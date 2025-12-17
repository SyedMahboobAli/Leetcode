# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            # height of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # update diameter (number of edges)
            self.diameter = max(self.diameter,left+right)
            # return height of current node
            return 1 + max(left,right)
        
        dfs(root) #this returns the height of root. don't return this. We are calling this method to populated self.diameter
        return self.diameter

'''
The diameter of a binary tree is the length of the longest path between any two nodes.
The diameter is measured in number of edges, not nodes. (n-1)
The longest path through that node is
👉 left_height + right_height
Algo:
Use DFS to compute height
While returning height, update the diameter
'''
