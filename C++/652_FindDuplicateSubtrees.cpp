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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int> maps;
        vector<TreeNode*> res;
        dfs(root, maps, res);
        return res;
    }
    
    string dfs(TreeNode* root, unordered_map<string,int>& maps, vector<TreeNode*>& res)
    {
        if (root == NULL) return "";
        string s = to_string(root->val) + "," + dfs(root->left, maps, res) + "," + dfs(root->right, maps, res);
        if (maps[s]++ == 1) res.push_back(root);
        return s;
    }
};