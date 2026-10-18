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
    vector<int> values;

    int kthSmallest(TreeNode* root, int k) {
        inOrder(root);
        return values[k - 1];
    }

    void inOrder(TreeNode* root){
        if(!root){
            return;
        }

        inOrder(root->left);
        values.push_back(root->val);
        inOrder(root->right);
    }
};
