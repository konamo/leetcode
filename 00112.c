/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool dfs(struct TreeNode *node, int targetSum)
{
    if (targetSum == node->val && node->left == NULL && node->right == NULL) {
        return true;
    }

    if (node->left) {
        bool ret = dfs(node->left, targetSum - node->val);
        if (ret == true)
            return true;
    }


    if (node->right) {
        return dfs(node->right, targetSum - node->val);
    }
    return false;
}


bool hasPathSum(struct TreeNode* root, int targetSum)
{
    if (root == NULL) {
        return false;
    }

    return dfs(root, targetSum);
}
