/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode SufficientSubset(TreeNode root, int limit) {
        if (root.left == root.right){
            if (root.val < limit){
                return null;
            } else{
                return root;
            }
        }
        if (root.left != null){
            root.left = SufficientSubset(root.left, limit-root.val);
        }
        if (root.right != null){
            root.right = SufficientSubset(root.right, limit-root.val);
        }
        if (root.left != null || root.right != null){
            return root;
        } else{
            return null;
        }
    }
}