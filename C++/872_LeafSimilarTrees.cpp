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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> a, b;
        traverse(root1, a);
        traverse(root2, b);
        return a == b;
    }
    
    void traverse(TreeNode* root, std::vector<int>& res)
    {
        if (!root->left && !root->right) res.push_back(root->val);
        if (root->left) traverse(root->left, res);
        if (root->right) traverse(root->right, res);
        return;
    }
};