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
#include <ranges>
#include <string_view>

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "null";

        return to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        auto parts = data | views::split(',') | ranges::to<vector<string>>();
        int i = 0;

        return deserializeDfs(parts, i);
    }
private:
    TreeNode* deserializeDfs(vector<string>& parts, int& i){
        if(parts[i] == "null"){
            i++;
            return nullptr;
        }

        TreeNode* node = new TreeNode(stoi(parts[i]));
        i++;

        node->left = deserializeDfs(parts, i);
        node->right = deserializeDfs(parts, i);

        return node;
    }
};
