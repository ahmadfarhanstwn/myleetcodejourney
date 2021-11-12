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
    public IList<int> GetAllElements(TreeNode root1, TreeNode root2) {
        List<int> visited = new List<int>();
        Queue<TreeNode> q1 = new Queue<TreeNode>();
        Queue<TreeNode> q2 = new Queue<TreeNode>();
        if (root1 != null)
            q1.Enqueue(root1);
        if (root2 != null)
            q2.Enqueue(root2);
        while (q1.Count != 0){
            TreeNode node = q1.Dequeue();
            visited.Add(node.val);
            if (node.left != null)
                q1.Enqueue(node.left);
            if (node.right != null)
                q1.Enqueue(node.right);
        }
        while (q2.Count != 0){
            TreeNode node = q2.Dequeue();
            visited.Add(node.val);
            if (node.left != null)
                q2.Enqueue(node.left);
            if (node.right != null)
                q2.Enqueue(node.right);
        }
        visited.Sort();
        return visited;
    }
}