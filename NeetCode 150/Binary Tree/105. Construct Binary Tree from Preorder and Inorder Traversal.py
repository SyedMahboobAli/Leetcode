# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #hashmap sol
        inorder_map = {val:i for i,val in enumerate(inorder)}
        self.pre_ind = 0

        def dfs(left,right):
            if left > right : 
                return
            
            root = TreeNode(preorder[self.pre_ind])
            self.pre_ind += 1

            mid = inorder_map[root.val]

            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)

            return root
        
        return dfs(0,len(inorder) - 1)

