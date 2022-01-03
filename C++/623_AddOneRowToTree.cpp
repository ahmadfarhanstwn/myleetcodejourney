/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) return new TreeNode(val,root, NULL);
        traverse(root, depth, 1, val);
        return root;
    }
    
    void traverse(TreeNode* root, int& depth, int depthNow, int val)
    {
        if (depthNow > depth) return;
        if (depthNow == depth-1)
        {
            root->left = new TreeNode(val, root->left, nullptr);
            root->right = new TreeNode(val, nullptr, root->right);
        }
        if (root->left) traverse(root->left, depth, depthNow+1, val);
        if (root->right) traverse(root->right, depth, depthNow+1, val);
        return;
    }
};