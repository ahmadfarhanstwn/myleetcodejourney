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
    int val = 0;
    TreeNode* convertBST(TreeNode* root) {
        if (root){
            if(root->right){
                convertBST(root->right);
            }
            val = val + root->val;
            root->val = val;
            if(root->left){
                convertBST(root->left);
            }
        }
        return root;
    }
};