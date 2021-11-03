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
    bool isValidBST(TreeNode* root) {
        TreeNode* current = root;
        stack<TreeNode*> stack;
        vector<int> visited;
        while(true){
            if (current != NULL){
                stack.push(current);
                current = current->left;
            } else if (!stack.empty()){
                current = stack.top();
                stack.pop();
                if (visited.size() != 0){
                    if (visited[visited.size()-1] >= current->val){
                        return false;
                    }
                }
                visited.push_back(current->val);
                current = current->right;
            } else{
                break;
            }
        }
        return true;
    }
};