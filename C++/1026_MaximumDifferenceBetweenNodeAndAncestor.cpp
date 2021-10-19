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
    int maxAncestorDiff(TreeNode* root) {
        if (!root) return 0;
        return helper(root);
    }
    
    int helper(TreeNode* root, int mn = 10001, int mx = 0){
        if (!root){
            return mx - mn;
        }
        mx = max(mx, root->val);
        mn = min(mn, root->val);
        return max(helper(root->left, mn, mx), helper(root->right,mn,mx));
    }
};