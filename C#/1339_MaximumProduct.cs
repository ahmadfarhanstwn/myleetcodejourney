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
    long sumTotal = 0, result = 0, sub;
    public int MaxProduct(TreeNode root) {
        sumTotal = getSum(root);
        getResult(root);
        return (int)(result%1_000_000_007);
    }
    
    public int getSum(TreeNode root)
    {
        if (root == null)
            return 0;
        return root.val + getSum(root.left) + getSum(root.right);
    }
    
    public long getResult(TreeNode root)
    {
        if (root == null)
            return 0;
        sub = root.val + getResult(root.left) + getResult(root.right);
        result = Math.Max(result, sub * (sumTotal - sub));
        return sub;
    }
}