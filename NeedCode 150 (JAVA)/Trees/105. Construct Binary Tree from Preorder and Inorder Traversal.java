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
    private int preorderIndex = 0;
    private Map<Integer,Integer> inorderMap = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i = 0; i < inorder.length;i++){
            inorderMap.put(inorder[i],i);
        }
        
        return build(preorder,0,inorder.length-1);
    }

    private TreeNode build(int[] preorder, int left, int right){
        if(left > right) return null;

        int rootval = preorder[preorderIndex++];

        TreeNode root = new TreeNode(rootval);

        int inorderIndex = inorderMap.get(rootval);

        root.left = build(preorder,left,inorderIndex-1);
        root.right = build(preorder,inorderIndex+1,right);
        
        return root;

    }
}
