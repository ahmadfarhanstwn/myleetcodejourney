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
    long sumTotal = 0, result = 0, sub;
    int maxProduct(TreeNode* root) {
        sumTotal = getSum(root);
        getMaxProduct(root);
        return result % (int)(1e9 + 7);
    }
    
    int getSum(TreeNode* root)
    {
        if (!root)
            return 0;
        return root->val+getSum(root->left) + getSum(root->right);
    }
    
    int getMaxProduct(TreeNode* root)
    {
        if (!root)
            return 0;
        sub = root->val + getMaxProduct(root->left) + getMaxProduct(root->right);
        result = max(result, sub * (sumTotal - sub));
        return sub;
    }
};