/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }

    private int dfs(TreeNode node, int maxSoFar){
        if (node == null) return 0;
        
        int count = 0;
        if(node.val >= maxSoFar){
            count = 1;
            maxSoFar = node.val;
        }

        count += dfs(node.left,maxSoFar);
        count += dfs(node.right,maxSoFar);

        return count;
    }
}
