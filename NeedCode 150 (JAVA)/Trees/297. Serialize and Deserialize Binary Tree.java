/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        dfsSerialize(root,sb);
        return sb.toString();
    }

    private void dfsSerialize(TreeNode node, StringBuilder sb){
        if(node == null){
            sb.append("null,");
            return;
        }

        sb.append(node.val).append(",");
        dfsSerialize(node.left,sb);
        dfsSerialize(node.right,sb);
    }



    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return dfsDeserialize(queue);
    }

    private TreeNode dfsDeserialize(Queue<String> queue){
        String val = queue.poll();

        if(val.equals("null")){
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(val));

        root.left = dfsDeserialize(queue);
        root.right = dfsDeserialize(queue);

        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
