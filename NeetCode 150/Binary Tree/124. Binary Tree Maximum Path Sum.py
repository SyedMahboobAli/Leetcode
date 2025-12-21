# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right),0)

            #Two Possibilities:
            #1. If this node is part of the path which includes left and right childs, for which we update max_sum
            path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum,path_sum)

            #2. Send Gain in curr path to higher node, where current path goes from left child or right which ever is more.
            return node.val + max(left_gain,right_gain)
        
        dfs(root)
        return self.max_sum #Valid for case 1 and case 2 as in case 2 this may or maynot be included but max_sum is already computed
