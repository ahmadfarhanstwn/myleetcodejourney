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
    unordered_map<int, int> output;
    int maxOutput = 0;
    vector<int> findFrequentTreeSum(TreeNode* root) {
        traverse(root);
        vector<int> res;
        for (auto c: output){
            if (c.second == maxOutput){
                res.push_back(c.first);
            }
        }
        return res;
    }
    
    int traverse(TreeNode* node) {
        if (node == NULL) return 0;
        int s = node->val + traverse(node->left) + traverse(node->right);
        maxOutput = max(maxOutput, ++output[s]);
        return s;
    }
};