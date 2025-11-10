# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Approach 2: DFS and hasmap
        # Map each value to its index in inorder for O(1) lookup
        inorder_map = {val:ind for ind,val in enumerate(inorder)}
        self.pre_ind = 0 # pointer to current root in preorder

        def dfs(left,right):#These left/right are indices into the inorder array, not into preorder. instead of slicing preorder) avoids copying preorder
            # if there are no elements to construct subtrees
            if(left>right):
                return
            
            # Pick current root from preorder
            root_val=preorder[self.pre_ind]
            self.pre_ind+=1

            # Create root node
            root=TreeNode(root_val)

            # Split inorder list into left/right subtrees
            inorder_ind=inorder_map[root_val]

            # Build left and right subtrees
            root.left=dfs(left,inorder_ind-1)
            root.right=dfs(inorder_ind+1,right)

            return root

        return dfs(0,len(inorder)-1)

        #Approach 1: Recursion Not optimal
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) #we are going to update this in approach 2 by using Hashmap

        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid]) #since in inorder we have l > num > right. array all left numbers are in left subtree and right numbers are in right subtree we are using inorder[:mid]. for preorder[1:mid+1] because mid is index of inorder. => 0 to mid-1 are in left tree. in preorder after root, next elements are left and then right. [ all nodes in left subtree ] + [ all nodes in right subtree ]. count of left elements is mid. Since we are starting from 1, we need until mid+1
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
