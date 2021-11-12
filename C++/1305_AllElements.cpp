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
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> visited;
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;
        if (root1)
            q1.push(root1);
        if (root2)
            q2.push(root2);
        while (!q1.empty()){
            TreeNode* node = q1.front();
            visited.push_back(node->val);
            if (node->left)
                q1.push(node->left);
            if (node->right)
                q1.push(node->right);
            q1.pop();
        }
        while (!q2.empty()){
            TreeNode* node = q2.front();
            visited.push_back(node->val);
            if (node->left)
                q2.push(node->left);
            if (node->right)
                q2.push(node->right);
            q2.pop();
        }
        sort(visited.begin(), visited.end());
        return visited;
    }
};