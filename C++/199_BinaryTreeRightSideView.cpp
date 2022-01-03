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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (root) traverseRight(root, res, 1);
        return res;
    }
    
    void traverseRight(TreeNode* root, vector<int>& res, int depth) {
        if (depth > res.size()) res.push_back(root->val);
        if (root->right) traverseRight(root->right, res, depth+1);
        if (root->left) traverseRight(root->left, res, depth+1);
        return;
    }
};