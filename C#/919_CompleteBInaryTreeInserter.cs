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
public class CBTInserter {
    private List<TreeNode> tree;
    public CBTInserter(TreeNode root) {
        tree = new List<TreeNode>();
        tree.Add(root);
        for(int i = 0; i < tree.Count; ++i){
            if (tree[i].left != null){
                tree.Add(tree[i].left);
            }
            if (tree[i].right != null){
                tree.Add(tree[i].right);
            }
        }
    }
    
    public int Insert(int val) {
        int n = tree.Count;
        TreeNode newNode = new TreeNode(val);
        tree.Add(newNode);
        if (n % 2 == 1){
            tree[(n-1)/2].left = tree[tree.Count-1];
        } else{
            tree[(n-1)/2].right = tree[tree.Count-1];
        }
        return tree[(n-1)/2].val;
    }
    
    public TreeNode Get_root() {
        return tree[0];
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.Insert(val);
 * TreeNode param_2 = obj.Get_root();
 */