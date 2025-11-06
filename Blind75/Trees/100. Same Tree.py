# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Approach 1: Recursive DFS
        #base case
        if not p and not q: #both nodes are None, structure matches,subtree is identical.
            return True
        if not p or not q: #the structure is different.
            return False
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        
        #Approach 2: BFS
        queue=deque([(p,q)])
        while queue:
            node1,node2 = queue.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append((node1.left,node2.left))
            queue.append((node1.right,node2.right))
